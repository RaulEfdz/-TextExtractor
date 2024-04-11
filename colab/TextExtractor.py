# Importamos las bibliotecas necesarias
import cv2
import pytesseract
import numpy as np
from pdf2image import convert_from_bytes
import tempfile
import os
from google.colab import files

# Configuramos Tesseract-OCR si es necesario
# pytesseract.pytesseract.tesseract_cmd = r'<ruta_a_tesseract.exe>'

# Función para extraer texto de una imagen
def extract_text_from_image(image):
    # Convertimos la imagen a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Aplicamos un filtro gaussiano para reducir el ruido
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    # Utilizamos pytesseract para extraer el texto de la imagen
    extracted_text = pytesseract.image_to_string(blurred_image)
    return extracted_text

# Función para manejar archivos, puede ser imagen o PDF
def process_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.pdf':
        # Temporalmente almacenamos las imágenes extraídas del PDF
        images_from_path = convert_from_bytes(open(file_path, 'rb').read())
        for image in images_from_path:
            image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            print(extract_text_from_image(image_cv))
    else:
        # Proceso para imágenes
        image_cv = cv2.imread(file_path)
        print(extract_text_from_image(image_cv))

# Función para seleccionar y procesar el archivo
def upload_and_process():
    uploaded = files.upload()
    if len(uploaded) > 0:
        file_path = list(uploaded.keys())[0]
        print(f"Extrayendo texto de {file_path}:")
        process_file(file_path)
    else:
        print("No se ha seleccionado ningún archivo.")

# Llamamos a la función para subir y procesar el archivo
upload_and_process()
