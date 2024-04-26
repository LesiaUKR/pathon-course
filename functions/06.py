# Наступне завдання буде суто теоретичним, і ми потренуємося створювати
# функції в Python, які можуть приймати довільну кількість позиційних
# або ключових аргументів.

# Задачі:

# 1. Створіть функцію first, яка приймає один обов'язковий аргумент
# size та довільну кількість позиційних аргументів. Функція має
# повертати суму: size + кількість позиційних аргументів.
# 2. Створіть функцію second, яка також приймає один обов'язковий
# аргумент size та довільну кількість ключових аргументів.
# Функція має повертати суму: size + кількість ключових аргументів.
# В обох функціях використовуйте спеціальні синтаксиси * для
# позиційних аргументів та ** для ключових аргументів.
# Очікуваний результат:

# Функції повинні коректно розраховувати суму size та кількості
# переданих аргументів.

# Підказки:

# *args у функції first означає, що функція може приймати будь-яку
# кількість позиційних аргументів.
# **kwargs у функції second означає, що функція може приймати
# будь-яку кількість ключових аргументів.
# Використовуйте функцію len для визначення кількості позиційних
# або ключових аргументів.
# Приклад коду виконання функцій:

# print(first(5, "first", "second", "third"))  # Результат: 8
# print(first(1, "Alex", "Boris"))             # Результат: 3
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))  # Результат: 6
# print(second(10, comment_one="Alex", comment_two="Boris")) # Результат: 12

def first(size, *args):
    return size + len(args)


print(first(5, "first", "second", "third"))  # Результат: 8
print(first(1, "Alex", "Boris"))  # Результат: 3


def second(size, **kwargs):
    print(len(kwargs))
    return size + len(kwargs)


print(second(3, comment_one="first", comment_two="second", comment_third="third"))