# Импорты
import tarfile
from requests import get
import pandas as pd

# Ссылка на архив лога
url_test = "https://sysadmin.education-services.ru/downloads/nginx.log.tar.gz"
file_name_test = "nginx.log.tar.gz"

# Функция скачивания файла
def download(url, file_name):
    response = get(url)
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"[OK] Файл '{file_name}' успешно загружен.")
    else:
        print(f"[Ошибка] Не удалось скачать файл. Код состояния: {response.status_code}")

download(url_test, file_name_test)

# Распаковка архива
with tarfile.open(file_name_test, 'r:gz') as tar:
    tar.extractall('./')
    print("[OK] Архив распакован.")

# Чтение лог-файла
log_file_name = 'nginx.log'
with open(log_file_name, 'r') as file:
    lines = file.readlines()

# Просмотр первых 10 строк лога
print("Первые 10 строк лога:")
for i in range(min(10, len(lines))):
    print(f"({i+1}): {lines[i].strip()}")

# Количество строк в логе
print(f"\n[INFO] Всего строк в логе: {len(lines)}")

# Подсчет IP-адресов
ip_addresses = {}
for line in lines:
    if " - - " in line:
        current_ip = line.split(" - - ")[0]
        ip_addresses[current_ip] = ip_addresses.get(current_ip, 0) + 1

print(f"[INFO] Уникальных IP-адресов: {len(ip_addresses)}")

# Создание DataFrame и сортировка
df = pd.DataFrame(list(ip_addresses.items()), columns=["IP", "Количество"])
df_sorted = df.sort_values(by="Количество", ascending=False)

# Сохранение в файл
df_sorted.to_csv("result.txt", sep=":", index=False)
print("[OK] Результаты сохранены в 'result.txt'")
