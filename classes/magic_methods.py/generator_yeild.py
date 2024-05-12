# Генератор - це спрощений спосіб створення ітераторів
# Функція стає генератором, коли містить вираз yield
# Генератор автоматично реалізує методи __iter__() та __next__()

def count_down(start):
    current = start
    current -= 1
    while current >= 0:
        yield current
        current -= 1


# Використання генератора
for count in count_down(5):
    print(count)
