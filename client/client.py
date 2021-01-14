from base64 import b64encode, b64decode
import math
import json
import requests
import os
import glob
import shutil


url = 'http://localhost:8080/textract'
f = '/home/florian/projects/git/textract-docker/client/test.pptx'

with open(f, 'rb') as open_file:
    byte_content = open_file.read()
    base64_bytes = b64encode(byte_content)
    base64_string = base64_bytes.decode('utf-8')
    raw_data = {
        "data": base64_string,
        "file_type": f.split('.')[-1]
        }

#print(raw_data)



r = requests.post(url, json=raw_data)
print(r)
print(r.text)
print(r.json)





