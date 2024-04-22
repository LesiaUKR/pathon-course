#  символ \ в кінці першого та другого рядка коду, він вказує інтерпретатору
# ігнорувати закінчення рядка і продовжити відразу з наступного

one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."

# У Python, коли ви поміщаєте два рядкових літерали поруч,
# вони автоматично конкатенуються (об'єднуються в один рядок).
# Це відомо як неявна конкатенація рядків:
("spam " "eggs") == "spam eggs"  # True

# неявна конкатенація рядків:
one_line_text = ("Textual data in Python is handled with str objects,"
                 " or strings. Strings are immutable sequences of Unicode"
                 " code points. String literals are written in a variety "
                 " of ways: single quotes, double quotes, triple quoted.")

# в майбутньому, це дуже допомагає при створенні SQL запитів до бази даних:
query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")

# керувальні символи
# символ \n відповідає за перенос рядка (line break)
print("Hello\nWorld")

# горизонтальна табуляція \t (tab):
print("Hello\tWorld")  # При виведенні між словами буде символ табуляції

# повернення каретки \r (carriage return)
print("Hello\rWorld")  # При виведенні слово World замінить слово Hello
# При виведенні слово sister замінить слово little
print("Hello my little\rsister")

# Керувальний символ \b забій (backspace)
# Виведення здійснюється на один символ вліво та виконує вивід залишку після керувального символу.
print("Hello\bWorld")

# якщо нам треба виконати виведення зворотної косої риски
print("Hello\\World")

# екрануємо одинарні та подвійні лапки, щоб дозволити використовувати лапки всередині рядкових літералів
print('It\'s a beautiful day')
print("He said, \"Hello\"")


# методи рядків

# find - Для пошуку деякого символу або підрядка у рядку
# метод повертає індекс початку першого збігу в рядку s,
# починаючи з позиції start до позиції end.
# Якщо start та end не вказані, то пошук відбувається
# з початку і до кінця рядку. Метод повертає -1,
# якщо послідовність не знайдена.

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end))  # 5
print(s.find("q"))  # -1

# index - Цей метод аналогічний методу find,
# якщо index не знайде підрядок, то викличе виняток ValueError
# rindex - правий" аналог index

s = 'Some words'

print(s.index("o"))
print(s.rindex('o'))

# rfind - пошук підрядка у рядку справа, а не зліва як у find
s = 'Some words'

print(s.find("o"))
print(s.rfind('o'))


# split() - розділяє рядок на підрядки за вказаним роздільником
# Синтаксис методу split()
# str.split(separator=None, maxsplit=-1)
# separator - роздільник, за яким слід розділяти рядок.
# Якщо не вказано, рядок розділяється за будь-яким пробілом.
# maxsplit - максимальна кількість розділень.
# Значення -1 означає "без обмежень".
text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

text_2 = "apple,banana,cherry"
result_2 = text_2.split(',')
print(result_2)  # Виведе: ['apple', 'banana', 'cherry']


# join() - метод, який об'єднує елементи списку або кортежу в один рядок
# Синтаксис методу join()
# string.join(iterable)
# string - рядок роздільник, який буде вставлений між елементами послідовності.
# iterable - послідовність, список або кортеж рядків, які потрібно об'єднати.

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'

# strip() - метод, який видаляє пробіли з початку та кінця рядка
# lstrip() - видаляє пробіли з початку рядка
# rstrip() - видаляє пробіли з кінця рядка
clean = '   spacious   '.strip()
print(clean)  # spacious

# replace() - метод, який замінює один підрядок на інший
# Метод replace() має наступний синтаксис
# str.replace(old, new, count=-1)
# old - підрядок, який потрібно замінити.
# new - підрядок, на який потрібно замінити.
# count - лічильник максимальної кількості замін.
# якщо не вказано або вказано -1, замінюються всі входження.
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text)

# Якщо нам треба обмеження кількості замін, то:

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)

# Метод replace() також застосовують для видалення підрядка з рядка.

text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text)

# removeprefix() - видалення фіксованої послідовності на початку рядка
print('TestHook'.removeprefix('Test'))  # Hook
# TestHook - 'Hook' це суфікс рядка і видалений не буде
print('TestHook'.removeprefix('Hook'))

# removesuffix() - видалення фіксованої послідовності на кінці рядка
print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))


# Ви маєте URL пошукового запиту, і ваше завдання - видобути та обробити параметри цього запиту
# <https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>

# отримуємо частину запиту з URL
url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

# операція url_search.split('?') розділяє URL на дві частини: до знаку ? та після.
# Оскільки нас цікавить лише частина після ?, ми використовуємо символ _ для
# ігнорування частини URL до ?. Та отримуємо змінну query яка рядок,
# що містить необхідні нам параметри запиту.

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)

# isdigit() - метод, який перевіряє, чи складається рядок лише з цифр

number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False

# для перевірки, чи ввів користувач число
user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")

# перевірку на цифрові символи в рядку.
for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")

# translate() - метод, який використовується для перетворення
# рядків шляхом заміни певних символів іншими символами
# перш ніж використовувати translate(), нам потрібно створити таблицю перекладу
# Це можна зробити за допомогою методу str.maketrans(), який приймає два аргументи:
# Рядок символів, які потрібно замінити.
# Рядок символів, на які потрібно замінити.
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))  # Th3s 3s str3ng 2x1mpl2
#  всі голосні літери 'a', 'e', 'i', 'o', 'u' у рядку
# замінюються відповідно на числа '1', '2', '3', '4', '5'

# видалення певних символів із рядка.
# Для цього передайте в maketrans() третій аргумент - рядок символів, які потрібно видалити.
intab = "aeiou"
trantab = str.maketrans('', '', intab)

str = "This is string example"
print(str.translate(trantab))  # Ths s strng xmpl

# Наприклад нам треба розробити програму, яка конвертує рядок,
# що містить шістнадцяткові числа (в якості окремих символів),
# у відповідний двійковий код.

# Програма повинна обробляти як великі, так і малі літери
# шістнадцяткових чисел і перетворювати кожен символ на
# його чотирибітове двійкове представлення.

# zip(symbols, code)-який створює пари символ-двійковий код

symbols = "0123456789ABCDEF"
code = [
    '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
    '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 DF 56 AC".translate(MAP)
print(result)  # 00110100 11011111 01010110 10101100
print(MAP)  # ключ це Unicode для символів "0123456789ABCDEF" в верхньому та нижньому регістрі
# а значення відповідні елементи списку code

# Функція ord() в Python - це вбудована функція, яка приймає символ
# і повертає його Unicode код, який є цілим числом.


morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# розробити програму, яка перетворює вхідний текстовий рядок на відповідний код мови Морзе
# Перетворення ключів словника на Unicode коди

table_morze_dict = {}
# для кожного ключа словника morze_dict використовуючи функцію ord(k)
# додає до словника table_morze_dict Unicode ключі
# та відповідні коди Морзе - значеннями
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v
    print(table_morze_dict)
string = "Hello world"

result = ""

# перетворюємо рядок string в рядок result але вже азбукою Морзе
for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)  # .... . .-.. .-.. --- / .-- --- .-. .-.. -..

# Ми виконуємо ініціалізацію змінної result для зберігання результату.
# Після цикл for проходить по кожному символу рядка string.
# За допомоги методу ch.upper() перетворюємо символ у верхній регістр,
# щоб відповідати ключам у таблиці table_morze_dict.
# Метод translate(table_morze_dict) використовується для заміни
# кожного символу його відповідником у мові Морзе згідно з
# таблицею table_morze_dict. Результат додається до result.

# В кінці виконання коду змінна result містить перетворений рядок
# у мові Морзе, який виводиться на екран.


# вивести числа від 1 до 15 в десятковому, шістнадцятковому, вісімковому
# і двійковому представленні можна наступним чином:

for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

# int: 0;  hex: 0x0;  oct: 0o0;  bin: 0b0
# int: 1;  hex: 0x1;  oct: 0o1;  bin: 0b1
# int: 2;  hex: 0x2;  oct: 0o2;  bin: 0b10
# int: 3;  hex: 0x3;  oct: 0o3;  bin: 0b11
# int: 4;  hex: 0x4;  oct: 0o4;  bin: 0b100
# int: 5;  hex: 0x5;  oct: 0o5;  bin: 0b101
# int: 6;  hex: 0x6;  oct: 0o6;  bin: 0b110
# int: 7;  hex: 0x7;  oct: 0o7;  bin: 0b111

price = 19.99
quantity = 3
total = f"Total: {price * quantity:.2f}"
print(total)

# :.2f - це форматування числа з плаваючою точкою з двома знаками після коми
# : вводить специфікацію формату.
# .2 означає, що після десяткової крапки має бути виведено дві цифри.
# f вказує на формат дійсного числа.





