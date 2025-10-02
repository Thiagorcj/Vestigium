import gdown
import zipfile
import os


file_id = "1_P7Td9NzkV-7hj5O8k-C-OW7UGN5IjKC"
url = f"https://drive.google.com/uc?id={file_id}"
output = "paintings_dataset.zip"

# Baixar 
if not os.path.exists("dataset"):
    print("Baixando dataset do Google Drive...")
    gdown.download(url, output, quiet=False)

    # Extrair dataset.zip
    with zipfile.ZipFile(output, "r") as zip_ref:
        zip_ref.extractall("dataset")
    print("Dataset extraído em 'dataset/'")
else:
    print("Dataset já existe.")

