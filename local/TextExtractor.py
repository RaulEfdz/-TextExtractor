# Importamos las bibliotecas necesarias
import cv2
import pytesseract
import numpy as np
from pdf2image import convert_from_path
import tempfile
import os

# Especifica la ruta de Tesseract-OCR si es necesario
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
    if file_path.lower().endswith('.pdf'):
        # Temporalmente almacenamos las imágenes extraídas del PDF
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(file_path, output_folder=path)
            for image in images_from_path:
                image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                print(extract_text_from_image(image_cv))
    else:
        # Proceso para imágenes
        image_cv = cv2.imread(file_path)
        print(extract_text_from_image(image_cv))

# Función para seleccionar y procesar el archivo
def upload_and_process():
    file_path = input("Introduce la ruta del archivo a procesar: ")
    if os.path.exists(file_path):
        print(f"Extrayendo texto de {file_path}:")
        process_file(file_path)
    else:
        print("El archivo no existe. Por favor, verifica la ruta.")

# Llamamos a la función para subir y procesar el archivo
upload_and_process()
