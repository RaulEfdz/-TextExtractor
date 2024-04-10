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


 # EL CODIGO ESTA EN: TextExtractor.py
