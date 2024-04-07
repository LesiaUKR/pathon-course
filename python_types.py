# string, int, boolean, float, list, set, tuple, None

# рядок
# str 'Bogdan'
print(str("Bohdan"))  # Bohdan
print(ord("B"))  # 66 - код символа в таблиці ASCII
name = "Kate"
nameTwo = "Oleh"
print(name + nameTwo)  # KateOleh - конкатенація рядків
print("name" * 32)  # namenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenamenameenamenamenamenamenamename
print("name" + 32)  # TypeError: can only concatenate str (not "int") to str
"e" in "Kate"  # True - перевірка чи є символ в рядку

# int 10 - ціле число
# age = 18
# print(type(age))

# float - дробове число
age = 18.5
print(type(age))
print(float(2))  # 2.0

# boolean true - логічні
# bool True
# bool False
# a = 2
# print(type(a)) # <class 'int'>
a = False
print(type(a))  # <class 'bool'>
print(int(a))  # 0
print(int(True))  # 1
print(int())  # 0 значення за замовчуванням

# список
# list [1,2,3]

# словник
# dict {'min':5, 'max':8

# None
a = None
print(a)  # None
# щоб перевірити чи змінна має значення None потрібно використовувати оператор is
# is перевіряє і типи даних і значення
# оператор is - аналог === в JavaScript
a is None  # True - поверне True, якщо змінна має значення None
1 is None  # False - поверне False, якщо змінна не має значення None

True and False and False  # False
(True and False and False) or True  # True
False and True and True  # False
False and 1/0  # False
False or 1/0  # mistake ZeroDivisionError: division by zero
not False  # True
not True  # False
bool("as")  # True
bool("")  # False
bool(" ")  # True
len("as")  # 2
len("")  # 0
len(" ")  # 1
