cars = {
    "Ford": 2005,
    "Mitsubishi": 2000,
    "BMW": 2019,
    "VW": 2005,
}
# return a message with a list of cars sorted by name
# отримуємо список ключів словника
names = list(cars.keys())
# сортуємо його
names.sort()
# виводимо через розділювач
print(" | ".join(names))
