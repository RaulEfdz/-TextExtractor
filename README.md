TextExtractor: Herramienta de Extracción de Texto de Imágenes y PDFs
TextExtractor es una herramienta eficaz para extraer texto de documentos en formatos de imagen y PDF. Basada en la potente combinación de Tesseract-OCR para el reconocimiento óptico de caracteres y OpenCV para el procesamiento de imágenes, TextExtractor simplifica la obtención de texto de documentos complejos. Se integra además con pdf2image para la conversión de documentos PDF en imágenes procesables, mejorando así la accesibilidad y manipulación del contenido textual.

Características:
Extrae texto de archivos en formatos de imagen y PDF.
Aplica técnicas de pre-procesamiento de imágenes para mejorar la precisión del OCR.
Soporta la conversión de páginas PDF a imágenes para su procesamiento.
Cómo Utilizar:
Instalación de Dependencias:
Para comenzar, instala las dependencias necesarias ejecutando los siguientes comandos:

diff
Copy code
!pip install pytesseract pdf2image
!apt-get install tesseract-ocr poppler-utils -y
Asegúrate de estar en un entorno que permita la ejecución de estos comandos, como Google Colab.

Implementación del Código:

Importa las bibliotecas requeridas al inicio de tu script.
Copia las funciones extract_text_from_image y process_file en tu script para habilitar la extracción de texto.
Uso:

Sube el archivo (imagen o PDF) que deseas procesar.
Llama a process_file con la ruta del archivo subido para iniciar la extracción de texto.
Ejemplo de uso para un archivo llamado "documento.pdf":

python
Copy code
file_path = "documento.pdf"  # Asume que el archivo ya está accesible
print(f"Extrayendo texto de {file_path}:")
process_file(file_path)
Este enfoque directo y eficaz te permite acceder y manipular el contenido textual de documentos y imágenes con facilidad.


------------

# TextExtractor: Herramienta de Extracción de Texto de Imágenes y PDFs

**TextExtractor** es una herramienta eficaz diseñada para extraer texto de documentos en formatos de imagen y PDF. Utilizando una potente combinación de **Tesseract-OCR** para el reconocimiento óptico de caracteres y **OpenCV** para el procesamiento de imágenes, **TextExtractor** facilita la obtención de texto de documentos complejos. Además, integra **pdf2image** para convertir documentos PDF en imágenes procesables, mejorando así la accesibilidad y manipulación del contenido textual.

## 🌟 Características

- Extrae texto de **archivos en formatos de imagen y PDF**.
- **Aplica técnicas de pre-procesamiento de imágenes** para mejorar la precisión del OCR.
- **Soporta la conversión de páginas PDF a imágenes** para su procesamiento.

## 🚀 Cómo Utilizar

### 📌 Instalación de Dependencias

Instala las dependencias necesarias ejecutando los siguientes comandos:


!pip install pytesseract pdf2image
!apt-get install tesseract-ocr poppler-utils -y
Nota: Estos comandos son adecuados para ambientes como Google Colab.

##📝 Implementación del Código
Importa las bibliotecas requeridas al inicio de tu script.
Copia las funciones extract_text_from_image y process_file en tu script para habilitar la extracción de texto.
🖥 Uso
Sube el archivo (imagen o PDF con imagenes ) que deseas procesar.
Llama a process_file con la ruta del archivo subido para iniciar la extracción de texto.
Ejemplo de uso para un archivo llamado "documento.pdf":
python


![image](https://github.com/RaulEfdz/-TextExtractor/assets/68834789/6b96fecc-ef38-4ccc-8194-a9a9313d1cd8)
