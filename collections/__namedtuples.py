import collections
from collections import namedtuple

# namedtuple - іменовані кортежі - це кортежі, у яких кожен елемент має ім'я, а також індекс, тобто
# вони поєднують в собі можливості кортежів і словників

# Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])

# Створення екземпляра Point
p = Point(11, y=22)

# Доступ до елементів
print(p.x)  # 11
print(p.y)  # 22


person = ('Mick', 'Nitch', 35, 'Boston', '01146')

# Створення іменованого кортежу Person
Person = namedtuple(
    'Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# Виведення різних атрибутів іменованого кортежу
print(person.first_name)
print(person.post_index)
print(person.age)
print(person[3])


Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')
