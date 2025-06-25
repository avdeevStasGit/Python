from requests import get

# Link to the log file.
url = "https://sysadmin.education-services.ru/downloads/nginx.log.tar.gz"
# The name of the log file.
file_name = "nginx.log.tar.gz"

# Функция скачивание файла лога.
def download(url, file_name):
    with open (file_name, "wb") as file:
        response = get(url)
        file.write(response.content)