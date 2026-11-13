import sqlite3
from flask import Flask, jsonify, request
from app.descuentos import calcular_precio_final


def create_app(db_path='productos.db'):
    app = Flask(__name__)

    def db():
        con = sqlite3.connect(db_path)
        con.row_factory = sqlite3.Row
        return con

    with db() as con:
        con.execute(
            'CREATE TABLE IF NOT EXISTS productos ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT, '
            'nombre TEXT NOT NULL, precio REAL NOT NULL)'
        )

    @app.post('/productos')
    def crear_producto():
        datos = request.get_json(silent=True) or {}
        nombre = datos.get('nombre')
        precio = datos.get('precio')
        if not nombre or not isinstance(precio, (int, float)) or precio < 0:
            return jsonify(error='Datos inválidos'), 400
        with db() as con:
            cur = con.execute(
                'INSERT INTO productos (nombre, precio) VALUES (?, ?)',
                (nombre, precio),
            )
        return jsonify(id=cur.lastrowid, nombre=nombre, precio=precio), 201

    @app.get('/productos/<int:pid>/precio-final')
    def precio_final(pid):
        descuento = request.args.get('descuento', 0, type=float)
        with db() as con:
            fila = con.execute(
                'SELECT * FROM productos WHERE id = ?', (pid,)
            ).fetchone()
        if fila is None:
            return jsonify(error='No encontrado'), 404
        try:
            return jsonify(precio_final=calcular_precio_final(fila['precio'], descuento))
        except ValueError as e:
            return jsonify(error=str(e)), 400

    return app


if __name__ == '__main__':
    create_app().run(port=5001)