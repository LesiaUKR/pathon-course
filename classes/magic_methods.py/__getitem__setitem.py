# __getitem__ and __setitem__ are used to get and set values using square brackets
# використовуються для налаштування доступу до елементів об'єкта за допомогою індексації або ключів

# __getitem__ - визначає поведінку об'єкта при зверненні до нього через квадратні дужки.
# __getitem__ - приймає два аргументи: self і key. self - це об'єкт, до якого звертаються,
#  а key - індекс або ключ, за допомогою якого ви хочете отримати значення.


# __setitem__ - визначає, як об'єкт поводиться при встановленні значення через квадратні дужки.
# __setitem__ - приймає три аргументи: self, key і value. self - це об'єкт, до якого звертаються,


class SimpleDict:
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value


# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])
print(simple_dict['age'])


class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value {value} must be between {
                             self.min_value} and {self.max_value}")
        if index >= len(self.__data):
            # Додати новий елемент, якщо індекс виходить за межі
            self.__data.append(value)
        else:
            # Замінити існуючий елемент
            self.__data[index] = value

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.__data)


if __name__ == '__main__':
    temperatures = BoundedList(18, 26)

    for i, el in enumerate([20, 22, 25, 27]):
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)

    print(temperatures)
