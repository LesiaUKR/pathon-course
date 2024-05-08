class Person:
    pass  # Порожній блок для тіла класу


# class declaration - виклик конструктора класу Person() створює новий об'єкт класу Person
# p - instance, object, екземпляр класу Person
# () - виклик конструктора класу Person
p = Person()
print(p)  # <__main__.Person object at 0x000001D2D8B5F5B0>
print(type(p))  # <class '__main__.Person'>


# два об'єкти класу User: user1 та user2


class User:
    name = 'Anonymous'
    age = 15


user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = "John"
user2.age = 90

print(user2.name)
print(user2.age)

# Атрибут класу – це змінна, яка визначена на рівні класу, а не екземпляра класу.


class MyClass:
    class_attribute = "I am a class attribute"


# Поле класу(іноді називається "атрибут екземпляра") – це змінна,
# яка визначена на рівні окремого екземпляра класу. Кожен екземпляр
# класу має свій власний набір полів, які можуть приймати різні
# значення для різних екземплярів.
class MyClass:
    # constructor / initializer, not function but method
    # в init - можна записати різний код, який буде виконуватися
    def __init__(self, value):
        self.instance_field = value  # Поле класу


obj1 = MyClass(5)
obj2 = MyClass(10)

# Метод класу — це функція, яка оперує з полями класу
# та/або аргументами, які передаються у метод.
# Метод класу може бути викликаний як для класу, так і для екземпляра класу.


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age


bob = Person('Boris', 34)

bob.say_name()
bob.set_age(25)
bob.say_name()

# метод __init__() — спеціальний метод-конструктор, який автоматично
# виконується під час створення кожного нового екземпляра на базі класу Person.
# Ім'я методу починається і закінчується двома символами підкреслення.


# Змінна класу або атрибут – це змінна, яка зберігається в класі та доступ
# до них мають усі екземпляри цього класу.

# Змінна об'єкту або поле - це змінна, яка зберігається в об'єкті.
# Вона належать кожному окремому екземпляру класу.
# У цьому випадку кожен об'єкт має свою власну копію поля,
# тобто вона жодним чином не пов'язана з іншими такими
# ж полями в інших екземплярах.

# Тут count належить класу Person і є атрибутом класу.
# Його значення завжди одне й те саме для любого об'єкту класу.
# Змінна name належить об'єкту та є змінною об'єкту,
# і надає значення за допомогою self.
