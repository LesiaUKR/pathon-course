# Параметр *args - дозволяє передавати довільну кількість
#  позиційних аргументів, які зберігаються в кортежі.

# приймає довільну кількість позиційних аргументів

def print_all_args(*args):
    for arg in args:
        print(arg)


print_all_args(1, 'hello', True)

# виведення
# 1
# hello
# True


def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Hello", " ", "world", "!"))

# виведення
# Hello world!

# зазвичай це ім'я args, але може бути будь-яке інше ім'я


def concatenate(*strings) -> str:
    result = ""
    for arg in strings:
        result += arg
    return result


print(concatenate("Hello", " ", "world", "!"))

# параметр **kwargs - дозволяє передавати довільну кількість
# ключових аргументів, які зберігаються в словнику.


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


greet(name="Alice", age=25)

# виведення
# name: Alice
# age: 25
# kwargs зберігає словник, в нашому випадку це {'name': 'Alice', 'age': 25}


#!!! *args та **kwargs можна використовувати разом в одній функції
# Параметр *args повинен бути перед параметром **kwargs.
def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)


example_function(1, 2, 3, name="Alice", age=25)

# виведення
# Позиційні аргументи: (1, 2, 3) - кортеж
# Ключові аргументи: {'name': 'Alice', 'age': 25} - словник
