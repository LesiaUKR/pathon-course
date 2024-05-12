# @classmethod - на відміну від статичних методів, мають доступ до самого класу через параметр cls
# Класові методи часто використовуються для фабричних методів,
# які створюють екземпляри класу, використовуючи різні способи ініціалізації


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)


# Класові методи часто використовуються для фабричних методів,
# які створюють екземпляри класу, використовуючи різні
# способи ініціалізації, ніж стандартний конструктор

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)


employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)

print(john_doe.name)  # Виведе: John Doe
print(john_doe.position)  # Виведе: Manager


# Різниця між статичними та класовими методами полягає в тому,
# що статичні методи використовуються для функцій,
# які не потребують доступу до атрибутів або методів класу,
# тоді як класові методи мають доступ до класу та його атрибутів,
# дозволяючи змінювати стан класу або створювати екземпляри класу
# за допомогою альтернативних конструкторів.
