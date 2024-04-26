# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
# Виведе байтове представлення чисел b'\x00\x80\xff' в шістнадцятковому форматі
print(byte_numbers)
# \x є індикатором шістнадцяткового запису кожного байта


# функцією hex, яка перетворить ціле число в рядок — представлення числа в шістнадцятковій формі
for num in [127, 255, 156]:
    print(hex(num))  # 0x7f, 0xff, 0x9c

# bytearray - це змінювана версія байт-рядка, контейнер, який містить байти
# Основна відмінність від байт-рядків — це змінність, щоб змінити масив байтів, не потрібно створювати новий
# масив байтів сприймається системою як послідовність чисел від 0 до 255, а не як послідовність символів в ASCII кодуванні.
# Саме тому не можна написати byte_array[0] = b'B'

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)  # bytearray(b'Bill Kill')

# bytearray дозволяє додавати,видаляти,змінювати елементи
byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))
print(byte_array)

# bytearray можна легко перетворити в рядок за допомогою методу decode()
byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'

# порівняння рядків
string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")

# casefold() - метод, який перетворює рядок у нижній регістр, але враховує всі можливі варіанти
# casefold() є більш ефективним для мов, які мають особливі правила перетворення символів у різних регістрах
text = "Python Programming"
print(text.casefold())

# casefold()
german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")
