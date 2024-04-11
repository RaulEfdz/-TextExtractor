## Ejecución en Google Colab

Para ejecutar este código en Google Colab, sigue los siguientes pasos:

1. Abre Google Colab y crea un nuevo notebook o abre uno existente.

2. Crea dos celdas de código:

    - En la primera celda, copia y pega el siguiente código para instalar las bibliotecas necesarias:

    ```python
    !pip install opencv-python-headless pytesseract pdf2image
    ```

    - En la segunda celda, agrega el código de `colab/TextExtractor.py` que contiene las funciones y el flujo de trabajo para extraer texto de imágenes y archivos PDF.

3. Ejecuta ambas celdas en orden.

4. Después de ejecutar las celdas, podrás utilizar las funciones del archivo `colab/TextExtractor.py` para cargar archivos de imagen o PDF y extraer texto de ellos.


¡Listo! Ahora puedes utilizar el código en Google Colab para procesar tus archivos y extraer texto de ellos.
