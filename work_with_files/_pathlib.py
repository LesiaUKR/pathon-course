from pathlib import Path

# import os - може видалити програму, ширші можливості, можна працювати з операційною системою
# pathlib - краща версія os.path саме для роботи з файлами і папками, шляхами

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
