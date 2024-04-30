
import time
from pathlib import Path

file_path = Path("work_with_files/photos_unpacked/bot-icon.png")

# stat() повертає інформацію про файл, включаючи його розмір, час створення та час останньої модифікації.
file_info = file_path.stat()
print(file_info)

# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")