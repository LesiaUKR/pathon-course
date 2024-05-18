
class Car:
    instance = None
    # __new__ - конструктор класу, який викликається перед __init__
    # __new__ - відповідає за виділення пам'яті під об'єкт - memory allocation

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Car, cls).__new__(cls)
        return cls.instance

    def __init__(self, year, mark, model, color):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color

    def __repr__(self):
        return f"Car({self.year}, '{self.mark}', '{self.model}', '{self.color}')"

    def __str__(self):
        return (
            f"{self.store_name} - {self.mark}.{self.model}: {self.year}, {self.color}"
        )


car = Car(2016, "Zaz", "Forza", "White")
car2 = Car(2017, "Honda", "Honda", "black")
car3 = Car(2018, "Toyota", "Toyota", "red")
print(car, car2, car3)
print("---------------------")
# print(str(car))
print(repr(car))
# copy_car = eval(repr(car))
# print(copy_car.model)
