# Генератор в Python - це об'єкт, який використовується для лінивої (on-demand)
# генерації даних та дозволяє нам оголошувати функцію, яка може бути використана в циклі
# Генератор створюється за допомогою функції, яка повертає послідовність
# елементів один за одним, використовуючи yield, а не return
# Генератори можна перебирати в циклі for або вручну за допомогою функції next()

def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()

# Використання next()
print(next(gen))  # Виведе 1
print(next(gen))  # Виведе 2
print(next(gen))  # Виведе 3
print(next(gen))  # Виведе StopIteration

# для контролю винятку StopIteration найчастіше генератори використовуються
# безпосередньо в циклах for ..., який буде це виконувати за нас


def count_down(start):
    while start > 0:
        yield start
        start -= 1


for number in count_down(5):
    print(number)
