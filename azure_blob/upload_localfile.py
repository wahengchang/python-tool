from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
from azure.storage.blob import ContentSettings


AzureStorageAccount = "istagingstorage"
AzureStorageAccessKey = "qkFU/ah2v4cHvQ7oAZASb2HRGFUkJhg2xs5KBYB+2fEnYmSp6hZH9U3vEO6TujzHHdBF3HWVgqalwcUuvIBMUQ=="
AzureStorageContainerName = "peter-container"

block_blob_service = BlockBlobService(account_name=AzureStorageAccount, account_key=AzureStorageAccessKey)

block_blob_service.create_blob_from_path(
    AzureStorageContainerName,
    'out.jpg',
    'img.jpg',
    content_settings=ContentSettings(content_type='image/png')
            )
