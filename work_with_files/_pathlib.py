from pathlib import PurePath
from pathlib import Path

# import os - може видалити програму, ширші можливості, можна працювати з операційною системою
# pathlib - краща версія os.path саме для роботи з файлами і папками, шляхами
# pathlib - це модуль у Python, який надає класи для обробки файлових шляхів у об'єктно-орієнтованому стилі.
# Path та PurePath - два основних класи у цьому модулі
# Path наслідує всі методи з PurePath і додає методи для виконання операцій,
# які вимагають доступу до файлової системи, таких як читання,
# запис файлів, перевірка існування файлів тощо
# Path автоматично адаптується до особливостей шляхів у різних операційних системах

p = Path("work_with_files")
# print(p)
# print(type(p))

# print(p / "photos_unpacked" / "bot-icon.png")  # отримуємо шлях до файлу
# print("parent.p", p.parent)
# print("p.name", p.name)
# print("p.suffix", p.suffix)
# print(p.cwd())
# print(p.home())
# print(p.exists())
# print(p.is_dir())
# print(p.is_file())

# Об'єднання шляхів у pathlib
# Початковий шлях
base_path = Path("/usr/bin")

# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"

print(full_path)  # Виведе: /usr/bin/subdir/script.py

# виводимо всі файли і папки в папці, але не виводимо файли в папках, бо це не рекурсія


def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            print(f"This is folder: {el}")
        else:
            print(f"This is file: {el}")


# перебираємо всі файли в папках незалежно від вкладеності і виводимо назву файлу
# def parse_file(path):
#     for el in path.iterdir():  # iterdir - метод, який повертає по одному об'єкту
#         if el.is_dir():  # is_dir - метод, який перевіряє чи це папка
#             # рекурсія - якщо це папка, то викликаємо функцію parse_file, яка викликає сама себе і перебирає всі файли в папці
#             parse_file(el)
#             # якщо це файл, а не папка, то виводимо назву файлу
#         else:
#             print(f"This is file: {el}")


# parse_file(p)
parse_folder(p)

# PurePath - надає об'єктно-орієнтовані методи для маніпуляції шляхами без доступу до файлової системи
p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)
print("Suffix:", p.suffix)
print("Parent:", p.parent)

# read_text() - читає весь вміст файлу і повертає його як рядок
# Path.read_text(encoding=None, errors=None)

# encoding - необов'язковий, ім'я кодування, яке використовується
# для декодування файлу. Якщо не вказано, використовується
# кодування за замовчуванням.
# errors - необов'язково, інструкція, як обробляти помилки декодування.

# write_text() - записує рядок у файл
# Path.write_text(data, encoding=None, errors=None)
# data - рядок, який необхідно записати в файл.

# параметр errors, в обох методах, визначає, як мають бути оброблені ці помилки.
# errors='strict'. Це значення за замовчуванням. Якщо виникає помилка декодування,
# буде викинуто виключення UnicodeDecodeError.
# errors='ignore'. Якщо ми хочемо ігнорувати помилки декодування.
# Частини тексту, що не можуть бути декодовані, будуть просто пропущені.
# errors='replace'. Якщо пропускати ми не хочемо, то замінимо неможливі
# для декодування символи на спеціальний символ заміни, згідно документації символ '?'.


# Створення об'єкту Path для файлу
file_path = Path("work_with_files/example.txt")

# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")

# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text)

# read_bytes() та write_bytes() використовуються для читання та запису бінарних файлів відповідно
