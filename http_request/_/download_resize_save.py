
# im = Image.open("img.jpg")
# #im.rotate(45).show()
# im.resize(size,resample=0).show()

import os
import io
import requests
from PIL import Image
import tempfile

buffer = tempfile.SpooledTemporaryFile(max_size=1e9)
url = "https://www.gravatar.com/avatar/dd071a6a7c97ba637c558c5e71137c7b?s=32&d=identicon&r=PG"
r = requests.get(url, stream=True)
if r.status_code == 200:
    downloaded = 0
    filesize = int(r.headers['content-length'])
    for chunk in r.iter_content():
        downloaded += len(chunk)
        buffer.write(chunk)
        print(downloaded/filesize)
    buffer.seek(0)
    size = 180,90
    i = Image.open(io.BytesIO(buffer.read()))
    # i.resize(size,resample=0).save('out.jpg')
    i.resize(size,resample=0).save('out.jpg')
buffer.close()