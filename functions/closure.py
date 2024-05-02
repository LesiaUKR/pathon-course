# def outFn():
#     count = 0
#     def inFn():
#         nonlocal count
#         count +=1
#         return count
#     return inFn
# counter = outFn()
# print(counter()) #1
# print(counter()) #2

# Замикання (closure)
from typing import Callable


def closure():
    count = 0

    def add(n):
        nonlocal count
        count += n
        return count
    return add


my_add = closure()  # повернення функції add
print(my_add(5))

my_second_add = my_add
print(my_second_add(2))

# інші приклади замикань


def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


# Створення замикання
my_func = outer_function("Hello, world!")
my_func()


# створимо замикання, яке буде зберігати інформацію про кількість разів виклику функції
def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count
        count += 1
        return count

    return increment


# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3
