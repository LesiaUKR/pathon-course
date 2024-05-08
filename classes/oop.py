# OOP - object oriented programming

# Abstraction - це вибіркове незнання
# Encapsulation
# Polymorphism
# Inheritance


#  explain abstraction

# class declaration
class Animal:
    # constructor / initializer, not function but method
    # в init - можна записати різний код, який буде виконуватися
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


# виклик конструктора класу Person() створює новий об'єкт класу Person
# animal - instance, object, екземпляр класу Person
# () - виклик конструктора класу Person
animal = Animal("Simon", 4)
print(animal.nickname)
animal.age = 5
print(animal.get_info())


#  explain Inheritance
# (Animal) - клас, від якого наслідується клас Cat
class Cat(Animal):
    name = ["Cat"]

    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def get_info(self) -> str:
        return f"It's cat. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"


cat = Cat("Simon", 4, "Yurii")
print(cat.nickname)
cat.age = 5
print(cat.get_info())
print(cat.sound())
# print(cat.name)
# cat2 = Cat('Boris', 10, 'Sergey')
# cat2.name[0] ='Boris Animal'
# print(cat2.name)
# print(cat.name)
# print(Cat.name)
print(dir(cat))

#  explain polymorphism
# super() - виклик метода чи атрибута батьківського класу


class Dog(Animal):
    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def get_info(self) -> str:
        return f"It's dog. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Woof!"


cat = Cat("Simon", 4, "Yurii")
dog = Dog("Alisa", 7, "Vlad")

for el in (cat, dog):
    if type(el) is Dog:
        print(f"{el.sound()} {el.get_info()}")

print("--------------------")
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))
print(isinstance(dog, Dog))
print("--------------------")
print(type(dog) is Animal)
print(type(dog) is Dog)
print("------------------")

print(dog.get_info())
print(super(Dog, dog).get_info())
