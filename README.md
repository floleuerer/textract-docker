# Textract Webservice Docker-Image

A simple docker image to serve [textract](https://textract.readthedocs.io/) as a REST-API. Based on Python and [starlette](https://www.starlette.io).

## Supported file types

.csv via python builtins  
.doc via antiword  
.docx via python-docx2txt  
.eml via python builtins  
.epub via ebooklib  
.gif via tesseract-ocr  
.jpg and .jpeg via tesseract-ocr  
.json via python builtins  
.html and .htm via beautifulsoup4  
.mp3 via sox, SpeechRecognition, and pocketsphinx  
.msg via msg-extractor  
.odt via python builtins  
.ogg via sox, SpeechRecognition, and pocketsphinx  
.pdf via pdftotext (default) or pdfminer.six  
.png via tesseract-ocr  
.pptx via python-pptx  
.ps via ps2text  
.rtf via unrtf  
.tiff and .tif via tesseract-ocr  
.txt via python builtins  
.wav via SpeechRecognition and pocketsphinx  
.xlsx via xlrd  
.xls via xlrd  

## Build + Run

```
docker build -t textract .
docker run -t -p 8080:8080 -e PORT=8080 textract .
```

## Usage

See `client/client.py` for an example.

Request json:
```
{
    "data": <base64 encoded file data>,
    "file_type": <file type / extension e. g. png, txt, etc ... (without '.')>
}
```

Response json:
```
{
    "text": <extracted text utf-8 encoded>
}
```