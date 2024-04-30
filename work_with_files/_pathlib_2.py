"""
Sort files based on extensions
"""

from pathlib import Path
from shutil import copyfile

source = Path("work_with_files/photos_unpacked/")
output_folder = Path("work_with_files/Backup/")

# iterdir() використовується для отримання переліку всіх 
# файлів та піддиректорій у вказаній директорії
# mkdir() - створює нову директорію
# Path.mkdir(mode=0o777, parents=False, exist_ok=False)
# rmdir() - видаляє директорію, але директорія повинна бути порожньою

def read_folder(path: Path) -> None:
    for el in path.iterdir():
      #   якщо це папка, то викликаємо функцію read_folder, яка викликає сама себе і перебирає всі файли в папці
        if el.is_dir():
            read_folder(el)
        else:
          # якщо це файл, а не папка, то викликаємо функцію copy_file, яка копіює файли в папку output_folder
            copy_file(el)


def copy_file(file: Path) -> None:
   #  отримуємо розширення файлу
    ext = file.suffix.lstrip(".")
   #  створюємо папку з розширенням файлу в папці output_folder
    new_path = output_folder / ext
   # створюємо папку, якщо вона не існує, параметр exist_ok=True означає, що якщо папка вже існує, то не видає помилку
   # параметр parents=True означає, що створюємо всі папки, які не існують і з вкладеністю
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path / file.name)


# dist
read_folder(source)
