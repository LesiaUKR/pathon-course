# __iter__() - Метод повертає сам ітератор
# __next__() - метод повертає наступний елемент об'єкта ітерації
# StopIteration - Коли елементи ітератора закінчуються, має бути викинуто виняток StopIteration
# ітератор дозволяє нам перебирати елементи контейнера за допомогою циклу for- in
# ітератор зберігає поточний стан перебору та дозволяює отримувати наступний елемент
# за допомогою методу __next__().


# створимо простий ітератор

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current


if __name__ == '__main__':
    counter = CountDown(5)
    for count in counter:
        print(count)
