
# im = Image.open("img.jpg")
# #im.rotate(45).show()
# im.resize(size,resample=0).show()

import os
import io
import requests
from PIL import Image
import tempfile
import StringIO

from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings

AzureStorageAccount = "istagingstorage"
AzureStorageAccessKey = "qkFU/ah2v4cHvQ7oAZASb2HRGFUkJhg2xs5KBYB+2fEnYmSp6hZH9U3vEO6TujzHHdBF3HWVgqalwcUuvIBMUQ=="
AzureStorageContainerName = "peter-container"
block_blob_service = BlockBlobService(account_name=AzureStorageAccount, account_key=AzureStorageAccessKey)

blobname="out7.jpg"


buf= StringIO.StringIO()


def _getDownloadlink():
                baseurl = "https://"+AzureStorageAccount+".blob.core.windows.net/"
                downloadlink = baseurl+AzureStorageContainerName+"/"+blobname
                return downloadlink
# im.save(buf, format= 'JPEG')
# jpeg= buf.getvalue()

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
    i.resize(size,resample=0).save(buf, format= 'JPEG')

    temp= buf.getvalue()

    stream = io.BytesIO(temp)
    block_blob_service.create_blob_from_stream(AzureStorageContainerName,blobname,stream)
    print _getDownloadlink()
buffer.close()