## OPCIÓN 1: Instrucciones para Clonar el Notebook en Google Colab

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

---

## OPCIÓN 2: Instrucciones para Ejecutar en Google Colab

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

