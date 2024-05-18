import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 100}

# Серіалізація об'єкта в файл
with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)


# Десеріалізація об'єкта з файлу
with open('data.pickle', 'rb') as file:
    deserialized_data = pickle.load(file)

# Виведе вихідний об'єкт Python
print(deserialized_data)
