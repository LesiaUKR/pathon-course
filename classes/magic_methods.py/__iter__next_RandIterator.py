from random import randint

# клас реалізує два основних методи, які роблять його ітератором: __iter__() та __next__()

# Ітератор - це об'єкт, який дозволяє користувачу перебирати всі елементи
# контейнера без потреби знати внутрішню структуру контейнера.
# Реалізується за допомогою методів __iter__() та __next__().
# Метод __iter__() повертає об'єкт ітератора, а метод __next__() автоматично
# викликається циклом for або функцією next() для отримання наступного
# елемента контейнера. Щоб створити ітератор, потрібно визначити клас з цими двома методами.


class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)


if __name__ == '__main__':
    my_random_list = RandIterator(1, 20, 5)
#  використовуємо наш ітератор в циклі for
    for rn in my_random_list:
        print(rn, end=' ')
