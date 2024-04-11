# TextExtractor.py - Guía de Instalación y Uso

## Instrucciones para Clonar el Notebook en Google Colab

# 1- Google Colab

¡Hola a todos! 🚀

Para acceder al notebook y comenzar a trabajar en él, sigue estos pasos simples:

1. Ve a la carpeta del proyecto `TextExtractor\colab` donde se encuentra el archivo del notebook.
2. Descarga el archivo `.ipynb` del notebook a tu computadora local.
3. Abre Google Colab en tu navegador web: [Google Colab](https://colab.research.google.com/).
4. En Google Colab, haz clic en "Archivo" en la barra de menú superior.
5. Selecciona "Subir notebook..." en el menú desplegable.
6. Busca el archivo `.ipynb` que descargaste anteriormente y selecciónalo para cargarlo en Google Colab.
7. Ejecuta la primera celda de instalaciones y espera a que termine.
8. Ejecuta la segunda celda.
9. Selecciona tu imagen, imágenes o PDF con imágenes dentro.
10. Espera a que termine de extraer el texto.

Espero que estas instrucciones te ayuden a comenzar con tu proyecto. Si necesitas más ayuda, no dudes en preguntar. ¡Buena suerte! 💡

--------------------------------------------------------------------------------------------
# 2- LOCAL

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
