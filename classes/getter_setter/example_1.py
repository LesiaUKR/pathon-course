class Person:
    def __init__(self, age):
        # Спочатку встановлюємо __age як None
        self.__age = None
        # Використовуємо сеттер для встановлення віку, що дозволяє валідацію вхідного значення
        self.age = age

    @property
    def age(self):
        # Геттер повертає значення приватного поля
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")
        # Присвоєння валідного значення приватному полю
        self.__age = value


if __name__ == "__main__":
    person = Person(-10)
    print(person.age)

   #  person.age = -5 - cause error
# Traceback(most recent call last):
#   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic7\\ex25.py", line 19, in <module >
#     person.age = -5
#   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic7\\ex25.py", line 12, in age
#     # Валідація вхідного значення
#     raise ValueError("Вік не може бути від'ємним")
# ValueError: Вік не може бути від'ємним
