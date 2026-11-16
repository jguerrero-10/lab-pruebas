# Resultados de la prueba de carga (k6)

API local (Flask, servidor de desarrollo), endpoint GET /productos/1/precio-final.
Umbrales: p(95) < 500 ms y errores < 1 %.

| Usuarios | p(95) | % de errores | Cumple |
|---|---|---|---|
| 20 | 76,02 ms | 0,00 % | Si |
| 100 | 91,86 ms | 0,00 % | Si |
| 200 | 141,94 ms | 0,00 % | Si |
| 250 | 307,55 ms | 13,31 % | No |
| 300 | 238,91 ms | 24,19 % | No |

Punto de quiebre: entre 200 y 250 usuarios simultaneos.
Causa: agotamiento de puertos de Windows (error "Solo se permite un uso de cada
direccion de socket"). El servidor de desarrollo de Flask no reutiliza conexiones.
