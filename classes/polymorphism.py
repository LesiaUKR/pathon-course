class Animal:
    count = 0

    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age
        Animal.count += 1

    def get_info(self) -> str:
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


class Cat(Animal):
    count = 0

    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner
        Cat.count += 1

    def get_info(self) -> str:
        return f"It's cat. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"


class Dog(Animal):
    count = 0

    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner
        Dog.count += 1

    def get_info(self) -> str:
        return f"It's dog. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Woof!"


cat = Cat("Simon", 4, "Yurii")
dog = Dog("Alisa", 7, "Vlad")
cat2 = Cat("Boris", 10, "Sergey")
cat3 = Cat("Iris", 10, "Oleksandr")
dog2 = Dog("Rex", 5, "Vlad")

for el in (cat, dog):
    print(el.sound())
    if isinstance(el, Dog):
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

print("------------------")
print(Animal.count)
print(cat.count)
print(dog.count)
