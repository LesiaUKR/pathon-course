from __future__ import annotations

import json
import pickle


class User:
    # Custom class with all class variables given in the __init__()
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends

    # works for pickle only
    def __getstate__(self):
        print("ASdasd")
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        print("ASdsadsadsadsdsa")

    def to_json(self):
        return {
            "name": self.name,
            "contacts": self.friends
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


user = User(name="John", age=28, friends=[
            "Jane", "Tom"], balance=20.70, active=True)


# буде помилка TypeError: Object of type User is not JSON serializable, бо клас не є сереалізованим
# print(user)


# 1 спосіб десереалізації - використання методу to_json()
# буде працювати, бо ми викликаємо метод to_json()
# у своєму методі можна вказати, які поля сереалізувати і не показувати наприклад приватні поля
# якщо щось серйозне, то краще використовувати свій метод сереалізації
# res = json.dumps(user.to_json())
# print(res)

# другий спосіб десереалізації - використання __dict__
# сереалізує все, в тому числі приватні поля
# res = json.dumps(user.__dict__)
# print(res)

# запакуємо у файл
with open("data_user.json", "w", encoding="utf-8") as f:
    json.dump(user.__dict__, f)

# відкриємо файл
with open("data_user.json", "r", encoding="utf-8") as f:
    restore_data = json.load(f)
    print(restore_data)

# відновимо об'єкт
# ** - розпаковує словник
replica_user = User(**restore_data)
print(replica_user)
