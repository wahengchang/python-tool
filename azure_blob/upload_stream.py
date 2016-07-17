from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings
import requests
import io

AzureStorageAccount = "istagingstorage"
AzureStorageAccessKey = "qkFU/ah2v4cHvQ7oAZASb2HRGFUkJhg2xs5KBYB+2fEnYmSp6hZH9U3vEO6TujzHHdBF3HWVgqalwcUuvIBMUQ=="
AzureStorageContainerName = "peter-container"

blobname="out2.jpg"
url = "https://www.gravatar.com/avatar/dd071a6a7c97ba637c558c5e71137c7b?s=32&d=identicon&r=PG"

block_blob_service = BlockBlobService(account_name=AzureStorageAccount, account_key=AzureStorageAccessKey)

r = requests.get(url, stream=True)
stream = io.BytesIO(r.content)

block_blob_service.create_blob_from_stream(AzureStorageContainerName,blobname,stream)


def _getDownloadlink():
				baseurl = "https://"+AzureStorageAccount+".blob.core.windows.net/"
				downloadlink = baseurl+AzureStorageContainerName+"/"+blobname
				return downloadlink


	print _getDownloadlink()
