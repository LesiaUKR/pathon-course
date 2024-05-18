from __future__ import annotations

import pickle

# show load without class


class Car:
    store_name = "Autoria"

    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.store_name} - {self.mark}.{self.model}: {self.year}, {self.color}, '{self.price}'"


c = Car(2023, "Ford", "Fusion", "red", 12000)

# можна десеріалізевати бінарний рядок
# але якщо цей рядок отримати з іншого середовища, то можливо виникнуть проблеми
# якщо pickle не знайде оголошений клас, то він видасть помилку
a = b'\x80\x04\x95^\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x03Car\x94\x93\x94)\x81\x94}\x94(\x8c\x04year\x94M\xe7\x07\x8c\x04mark\x94\x8c\x04Ford\x94\x8c\x05model\x94\x8c\x06Fusion\x94\x8c\x05color\x94\x8c\x03red\x94\x8c\x05price\x94M\xe0.ub.'
deserialized_car = pickle.loads(a)
print(deserialized_car)

serialized_car = pickle.dumps(c)
print(serialized_car)
deserialized_car = pickle.loads(serialized_car)
print(deserialized_car)
print(c == deserialized_car)  # False - different objects
print(id(c), id(deserialized_car))  # different ids
