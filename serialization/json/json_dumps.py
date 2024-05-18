from __future__ import annotations

import json

# json - java script object notation - текстовий формат обміну даними, що базується на синтаксисі мови JavaScript
# deserialization = load(для файлу), loads (для строки)
# serialization = dump(для файлу), dumps(для строки)

d = {"a": 1}
l = [1, 2.2]
t = (3, 4)
s = "I am string!"
b = True
# set - не сереалізується, спочатку потрібно перетворити в рядок
st = {1, 2, "Test"}
obj = {"tuple": t, "list": l, "dict": d, "string": s, "bool": b}

# сереалізуємо у строку
serialized_str = json.dumps(obj)

print("serialized_str", serialized_str)
print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))


print(json.dumps(b))
# print(json.dumps(st)) # Error TypeError: Object of type set is not JSON serializable

# серіалізуємо у файл
with open("storage.json", "w") as f:
    json.dump(obj, f)
