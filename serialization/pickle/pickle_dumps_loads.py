import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data)
