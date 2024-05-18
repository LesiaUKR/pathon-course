# @classmethod - на відміну від статичних методів, мають доступ до самого класу через параметр cls
# Класові методи часто використовуються для фабричних методів,
# які створюють екземпляри класу, використовуючи різні способи ініціалізації
# cls - це посилання на клас, яке передається в метод як перший аргумент
# @staticmethod - метод який не має доступу до класу

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
    # створємо об'єкт через конструктор
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)

    @classmethod
    def get_default_employee(cls):
        return cls("Unknown", "Manager")

    @staticmethod  # метод який не має доступу до класу
    def get_employee_types():
        return [
            "Manager",
            "Developer",
            "TeamLead",
        ]
    # можна викликати через Employee.get_employee_type()

    def f(self):
        return Employee.get_employee_types()

    # для фабричних методів, коли потрібно створити кілька об'єктів
    @classmethod
    def get_n_Eployees(cls, n):
        employees = []
        for i in range(n):
            # в cls передається Employee
            employees.append(cls(f"Employee_{i}", i))
        return employees


employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)
res = Employee.get_default_employee()
print(res)
# фабричний метод, який створює список об'єктів
res2 = Employee.get_n_Eployees(5)
print(res2)
# статичний метод, який повертає список типів працівників
res3 = Employee.get_employee_types()
print(res3)
# print(john_doe.name)  # Виведе: John Doe
# print(john_doe.position)  # Виведе: Manager
# print(Employee.get_employee_types())

# Різниця між статичними та класовими методами полягає в тому,
# що статичні методи використовуються для функцій,
# які не потребують доступу до атрибутів або методів класу,
# тоді як класові методи мають доступ до класу та його атрибутів,
# дозволяючи змінювати стан класу або створювати екземпляри класу
# за допомогою альтернативних конструкторів.
