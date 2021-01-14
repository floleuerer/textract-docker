FROM python:3.8-buster

RUN apt-get update && apt-get install -y libxml2-dev libxslt1-dev antiword unrtf poppler-utils tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig 

RUN pip install aiohttp asyncio aiofiles uvicorn starlette textract python-pptx xlrd docx2txt

WORKDIR /workdir 
COPY app /workdir/

EXPOSE $PORT

ENTRYPOINT ["python", "-u", "server.py", "serve"]