class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form


# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")


def __init__(self, name, type, health):
    self.name = name  # Ініціалізація атрибута імені
    self.type = type  # Ініціалізація атрибута типу
    self.health = health  # Ініціалізація атрибута здоров'я


# створення екземпляру класу
pikachu = Pokemon("Pikachu", "Electric", 100)

# Виклик методу attack для pikachu, передаючи інший об'єкт Pokemon в якості аргументу.
pikachu.dodge()

# Виконуємо еволюцію pikachu в "Raichu", використовуючи метод evolve.
# Це змінить значення атрибуту name об'єкта pikachu на "Raichu".
pikachu.evolve("Raichu")
