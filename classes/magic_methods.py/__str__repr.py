# __str__ та __repr__ - представлення об'єкта у вигляді рядка
# __repr__ - представлення об'єкта у вигляді рядка для внутрішнього використання

# __repr__ - головне призначення - це створення офіційного рядкового представлення об'єкта,
# яке можна використати для відновлення об'єкта

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


original_point = Point(2, 3)
print(repr(original_point))   # Виводить: Point(x=2, y=3)

# Використання рядка, повернутого __repr__, для створення нового об'єкта
# за допомогою функції eval, яка і створює новий об'єкт new_point з рядкового представлення.
new_point = eval(repr(original_point))
print(new_point)

# __str__ - головне призначення - це створення неформального рядкового представлення об'єкта,
# яке можна використати для виводу на екран, має бути зрозумілим для людини
# має пріоритет над __repr__ при виклику функції print


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"

    def __repr__(self):
        return f"Human({self.name}, {self.age})"


human = Human("Alice", 30)
print(human)
