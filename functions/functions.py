def hello(name):  # name - параметр
    print("Hello there", name)
    print("Hi there", name)


print("Hello out of there")  # відобразиться першим, бо викликається першим

hello("Kate")  # Kate - аргумент
hello("Oleh")


def sum_nums(a, b):
    sum = a + b
    return sum

# якщо функція має return, то її виклик потрібно присвоїти змінній
# якщо функція не має return, то вона повертає None


first_sum = sum_nums(10, 20)
print(first_sum)
print(sum_nums(50.5, 20))
print(sum_nums(10, 20) + 30)
print(sum_nums(sum_nums(10, 20), 30))

print(print("Hello"))  # завжди виводить None, бо print не має return


def print_max(a, b):  # a, b - параметри
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')


print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів


# У Python немає синтаксичної різниці між функціями і процедурами
# функція вміє повертати деякий результат своєї роботи,
# а процедура нічого не повертає та результатом її роботи
# може бути зміна стану вже існуючих змінних

# Базовий синтаксис для повернення значення з функції

# def my_function() -> ReturnType:
#     # виконати дії
#     return result


# "type hints" - це анотації типів, які допомагають визначити типи
# "Type hints" в Python використовуються для вказівки очікуваних типів параметрів у функціях.

def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum


result = add_numbers(5, 10)
print(result)  # Виведе: 15

# Приклад функції, що повертає рядок


def greet(name: str) -> str:
    return f"Привіт, {name}!"


greeting = greet("Олексій")
print(greeting)  # Виведе: Привіт, Олексій!


# Функція, що повертає булеве значення
def is_even(num: int) -> bool:
    return num % 2 == 0


check_even = is_even(4)
print(check_even)  # Виведе: True


# Ключові аргументи функції
# Ключові аргументи у Python - це аргументи функції, які вказуються
# за їх іменем під час виклику функції.
#  Вони використовуються для
# передачі значень до функції, проте вони можуть бути вказані
# у будь-якому порядку, оскільки їх ім'я однозначно ідентифікує,
# якому параметру вони відповідають.
#  Використання ключових аргументів
# забезпечує більшу читабельність коду та дозволяє задавати значення
# за замовчуванням для аргументів функції.

def greet(name, message="Привіт"):
    print(f"{message}, {name}!")

# name — це позиційний параметр
# message — ключовий параметр зі
# значенням за замовчуванням "Привіт"


# використовує значення за замовчуванням для message
greet("Олексій")

# передача власного значення для message
greet("Марія", message="Добрий день")


def func(a, b=5, c=10):
    print('a дорівнює', a, ', b дорівнює', b, ', а c дорівнює', c)


# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)

# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)

# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)

# a дорівнює 3 , b дорівнює 7 , а c дорівнює 10
# a дорівнює 25 , b дорівнює 5 , а c дорівнює 24
# a дорівнює 100 , b дорівнює 5 , а c дорівнює 50


def say(message, times=1):
    print(message * times)


say('Привіт')
say('Світ', 5)


def real_cost(base: int, discount: int = 0) -> int:
    return base * (1 - discount)


price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)

print(f'Нова вартість хліба: {current_price_bread}')
print(f'Нова вартість масла: {current_price_butter}')
print(f'Нова вартість цукру: {current_price_sugar}')
