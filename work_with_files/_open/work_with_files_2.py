from pathlib import Path

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)


encoding: Windows, ASCII, UTF-16
UTF-8 is the dominant encoding for the World Wide Web (and internet technologies),
accounting for 98.2% of all web pages, 99.0% of the top 10,000 pages, and up to 100% for many languages,
as of 2024.[9] Virtually all countries and languages have 95% or more use of UTF-8 encodings on the web.

"""

# absolute path - це шлях відносно кореневого каталогу системи - C:\Users\user\OneDrive\Документы\GitHub\python-course\work_with_files\_open\ex_01.py
# relative path - це шлях, який відкритий в терміналі - work_with_files\_open\ex_01.py

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)


# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()

current_working_directory = Path(
    "E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04")
relative_path = absolute_path.relative_to(current_working_directory)
print(relative_path)

# write - перезаписує в файл, тобто попередні дані видаляються
# якщо файлу не існує, то він створюється
# w+ - файл в режимі для читання та запису, але сам файл ми перезаписуємо, якщо він існує

file = open("work_with_files/_open/test.txt", "w", encoding="utf-8")
file.write("Hello world!\n")
file.write("Hello Ukraine!\n")
# записує список рядків
file.writelines(["Hi Bob!", "Hi Dima!", "Test", "ups"])
file.close()

# read - читає весь файл
# r+ - файл в режимі для читання та запису, але сам файл ми перезаписуємо, якщо він існує
file = open("work_with_files/_open/test.txt", "r", encoding="utf-8")
# !!!!! size parameter
# result = file.read()
# result = file.readline()
result = file.readlines()
print(result)
file.close()

# append - дописує в кінець файлу
file = open("work_with_files/_open/test.txt", "a", encoding="utf-8")
file.write("\nUkraine won eurovision 2025\n")
file.write("\nUkraine won eurovision 2026\n")

# x - кожен раз створює новий файл, якщо файл існує, то видає помилку
file = open("work_with_files/_open/test_2.txt", "x", encoding="utf-8")


# b - бінарний режим
# .txt, csv, .json, .xml, .yaml - текстові файли - rt
# .jpg, .png, .gif, .mp3 - бінарні файли - rb
# rb - може зчитувати і текстові і бінарні файли
file = open("work_with_files/_open/p1.jpg", "rb")
print(file.read())
file.close()

# Бітові рядки - це рядки, які містять байти, а не символи
# Біт - це найменша одиниця інформації, яку можна зберігати в комп'ютері - 0 або 1
# Байт - це група бітів, яка складається з 8 бітів
# Один байт може представляти 256 різних станів
# Один байт може представляти 256 - Від 00000000 до 11111111 у двійковому форматі
# від 0 до 255 десятеричному
# можете використовувати методи ті що й для звичайних рядків upper(), startswith(), index(), find()
s = b'Hello!'
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

# wb - в цьому режимі у файл можна писати тільки байт-рядки або байт-масиви
# У режимі роботи з "сирими" даними можна відкрити та прочитати вміст будь-якого файлу
# Замість терміну “сирі” дані, можуть також казати двійкові дані або бінарні дані

with open('work_with_files/raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')

# якщо виникне якась помилка, то файл не буде закритий
file = open("work_with_files/_open/p1.jpg", "rb")
print(file.read())
# raise ValueError
file.close()  # цей рядок не виконається, бо вище виникне помилка
