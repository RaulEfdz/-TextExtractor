# TextExtractor.py - Guía de Instalación y Uso

## Requisitos Previos
- Python 3.6 o superior.
- pip (el gestor de paquetes de Python).

## Instalación de Dependencias

------------------------------------
- pip install -r requirements.txt -
------------------------------------

### Tesseract-OCR y Poppler-Utils

- **Windows**:
    - Descarga e instala **Tesseract** desde [la página oficial de GitHub](https://github.com/tesseract-ocr/tesseract/wiki).
    - Descarga e instala **Poppler** para Windows desde [aquí](http://blog.alivate.com.au/poppler-windows/).
    - Añade las rutas de Tesseract y Poppler a la variable de entorno `PATH`.

- **macOS**:
    ```bash
    brew install tesseract
    brew install poppler
    ```

- **Linux (Debian/Ubuntu)**:
    ```bash
    sudo apt-get update
    sudo apt-get install tesseract-ocr
    sudo apt-get install poppler-utils
    ```

## Configuración del Script

- Si Tesseract no está en tu `PATH` o necesitas especificar explícitamente la ruta, modifica `TextExtractor.py` añadiendo o editando la siguiente línea:

    ```python
    pytesseract.pytesseract.tesseract_cmd = r'<ruta_a_tesseract.exe>'
    ```

    Reemplaza `<ruta_a_tesseract.exe>` con la ruta correcta a Tesseract en tu sistema.

## Ejecución del Script

- En tu terminal o línea de comandos, navega hasta el directorio del proyecto y ejecuta:

    ```bash
    python TextExtractor.py
    ```

- Sigue las instrucciones en pantalla para cargar y procesar el archivo deseado.
