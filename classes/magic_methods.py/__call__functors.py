# functors - objects that can be called as functions
# функтори - об'єкти, які можна викликати як функції
# можуть приймати аргументи і повертати значення
# може зберігати стан між викликами
# можуть мати складну логіку виклику
# можуть бути використані для створення параметризованих,
# налаштовуваних або замкнутих функцій


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, other):
        return self.factor * other


# Створення екземпляра функтора
double = Multiplier(2)
triple = Multiplier(3)

# Виклик функтора
print(double(5))  # Виведе: 10
print(triple(3))  # Виведе: 9
