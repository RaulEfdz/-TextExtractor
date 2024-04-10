# Instalamos pytesseract
!pip install pytesseract

# Instalamos Tesseract-OCR
!apt-get install tesseract-ocr

# Instalamos pdf2image
!pip install pdf2image

# Instalamos poppler-utils, necesario para pdf2image
!apt-get install poppler-utils

# Importamos las bibliotecas necesarias
import cv2
import pytesseract
import numpy as np  # Importamos numpy
from google.colab import files
from pdf2image import convert_from_path
import tempfile

# Instalamos pytesseract
!pip install pytesseract

# Instalamos Tesseract-OCR
!apt-get install tesseract-ocr -y

# Instalamos pdf2image
!pip install pdf2image

# Instalamos poppler-utils, necesario para pdf2image
!apt-get install poppler-utils -y

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

# Subimos el archivo desde nuestro sistema local
uploaded = files.upload()

# Extraemos el texto del archivo subido
for file_name in uploaded.keys():
    print(f"Extrayendo texto de {file_name}:")
    process_file(file_name)
