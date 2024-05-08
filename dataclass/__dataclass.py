from dataclasses import dataclass


# @dataclass
# class ExampleClass:
#     attribute1: type
#     attribute2: type = default_value

# Традиційний спосіб створення класу для зберігання даних
# де потрібно визначити метод __init__ для ініціалізації атрибутів
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age


# Створення класу за допомогою декоратора dataclass
# @dataclass автоматично генерує метод __init__ та інші магічні методи,
# на основі оголошених атрибутів
# не першочергою, але можна використовувати для створення класів для зберігання даних
@dataclass
class Person:
    name: str
    age: int

# клас Article містить атрибути зі стандартними значеннями


@dataclass
class Article:
    title: str
    author: str
    views: int = 0
