# Imports.
import tarfile
from requests import get

# Link to the log file.
url_test = "https://sysadmin.education-services.ru/downloads/nginx.log.tar.gz"
# The name of the log file.
file_name_test = "nginx.log.tar.gz"

# Функция скачивание файла лога.
def download(url, file_name):
    with open (file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

# Extract the archive.
file = tarfile.open('nginx.log.tar.gz')
file.extractall('./')
file.close()

# Importing the log.
with open('nginx.log', 'r') as file:
    lines = file.readlines()

# Log analysis.
for line in range(10):
    print(f"(line): {lines[line]}")

# Колчество строк в логе.
len(lines)