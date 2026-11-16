# Informe de accesibilidad (Nivel 8)

- Fecha: 2026-11-16
- Objetivo: https://www.saucedemo.com (sitio público de práctica, solo pruebas suaves)
- Herramienta: Lighthouse 13.5.0 en Chrome (ventana de incógnito, escritorio, solo Accessibility)
- Entorno: Windows, Chrome

## Puntaje de referencia (automático)

| Página | Modo | Puntaje |
|---|---|---|
| Login | Navigation | 100 |
| Lista de productos (standard_user) | Snapshot | 100 |
| Resumen de compra (checkout-step-two) | Snapshot | 100 |
| Lista de productos (problem_user) | Snapshot | 100 |

Lighthouse no encontró fallos, pero solo detecta una parte de los problemas. La revisión manual sí encontró defectos.

## Problemas encontrados (priorizados)

| # | Problema | Elemento afectado | Criterio WCAG | Severidad |
|---|---|---|---|---|
| 1 | El foco del teclado se mueve pero no se ve ningún borde ni resaltado | Todos los elementos interactivos (menú, enlaces, botones Add to cart) | 2.4.7 Foco visible | Alta |
| 2 | Con problem_user las 6 imágenes de producto son el mismo archivo (sl-404) y no corresponden al texto alternativo | .inventory_item img en inventory.html | 1.1.1 Contenido no textual | Media |
| 3 | Tres paradas de Tab por producto: imagen y título llevan al mismo destino | item_N_img_link e item_N_title_link | 2.4.1 Evitar bloques / navegación eficiente | Baja |

## Revisiones superadas

- Orden de foco lógico: sigue el orden visual y los productos en orden alfabético.
- Zoom al 200 %: sin texto cortado.
- Mensaje de error del login: tiene role="alert" y el botón de cerrar tiene aria-label.

## Pasos para reproducir el hallazgo 1

1. Abrir https://www.saucedemo.com en Chrome e iniciar sesión con standard_user / secret_sauce.
2. Hacer clic en una zona vacía y pulsar Tab varias veces.
3. Resultado esperado: el elemento enfocado muestra un borde o resaltado.
4. Resultado real: no se ve ningún indicador (document.activeElement confirma que el foco sí se mueve).
