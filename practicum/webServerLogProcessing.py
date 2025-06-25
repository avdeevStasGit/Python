# Imports.
import tarfile
from requests import get
import pandas as pd


# Link to the log file.
url_test = "https://sysadmin.education-services.ru/downloads/nginx.log.tar.gz"
# The name of the log file.
file_name_test = "nginx.log.tar.gz"

# Функция скачивание файла лога.
def download(url, file_name):
    with open (file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

download(url_test, file_name_test)

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

# Количество строк в логе.
len(lines)

# Подсчет ip адресов.
ip_adresses = {}
for line in range(len(lines)):
    current_ip = lines[line].split(" - - ")[0]
    if current_ip in ip_adresses:
        ip_adresses[current_ip] += 1
    else:
        ip_adresses[current_ip] = 1

len(ip_adresses)

df = pd.DataFrame.from_dict(ip_adresses,orient='index')
df.head()
df.to_csv("./result.txt",sep=":")
df.sort_index()

