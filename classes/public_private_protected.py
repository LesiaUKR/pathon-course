# __weight - private
# _weight - protected
# weight - public
# mangle, mangling - __name -> _ClassName__name - to get access to private fields
# setter, getter - найкращий спосіб імплементації валідації даних
# @property - декоратор, який створює getter

# isinstance(nickname, [str, text]) - перевірка на тип даних, якщо nickname є str або text
# type(nickname) == str or type(nickname) == text - аналогічна перевірка на тип даних


class Animal:
    def __init__(self, nickname, age, weight):
      #   mangle, mangling
        self.__nickname = nickname
        self.__age = age
        self.__weight = weight

    @property  # getter
    def name(self):
        return self.__nickname

    @name.setter
    def name(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError("Give animal a name!")

    @name.deleter
    def name(self):
        print("Delete nickname")
        del self.__nickname

    @property  # без гетеру не можна доступитись до приватного поля
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in list(range(0, 50)):
            self.__age = age
        else:
            raise ValueError("Animals are not that old!")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Incorrect weight !")


chup = Animal("Chupakabra", 12, 100)
print(chup.name, chup.age, chup.weight)
print(chup._Animal__nickname)  # mangling - call private field

print("---------------------")
try:
    t_chup = Animal("Chupakabra", -3, 100)
    print(t_chup.name, t_chup.age, t_chup.weight)
    t_chup.weight = -5
except ValueError as err:
    print(err)
