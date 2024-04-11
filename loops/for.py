fruit = 'apple'
for char in fruit:
    print(char)

# побачите в консолі
# a
# p
# p
# l
# e


word = "Andrii Kateryna"
res = 0

for symbol in word:
    if symbol.lower() == 'a':
        res += 1

print(res)


alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")

# побачите в консолі
#  a b c d e f g h i j k l m n o p q r s t u v w x y z

some_iterable = ["a", "b", "c"]

for i in some_iterable:
    print(i)

# побачите в консолі
# a
# b
# c

# Користувач вводить рядок. Треба порахувати скільки символів
# в рядку та скільки пробілів в рядку.

# порядок дій для розв'язання цієї задачі:
# Зчитування рядка від користувача.
# Використання циклу for для перебору кожного символу в рядку.
# Підрахунок загальної кількості символів та окремо кількості
# пробілів за допомоги циклу for та оператору if.

# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")

# find min max


# range(start, stop, step) - generates a sequence of numbers from start to end with a step size of step
# range(stop): Створює послідовність чисел від 0 до stop - 1.
# range(start, stop): Генерує числа від start до stop - 1.
# range(start, stop, step): Створює числа від start до stop - 1, з кроком step.


for number in range(7):
    print(number)


# побачите в консолі
# 1, 2, 3, 4, 5, 6

for i in range(2, 10):
    print(i)

# побачите в консолі
# 2, 3, 4, 5, 6, 7, 8, 9

for i in range(0, 10, 2):
    print(i)

# побачите в консолі
# 0, 2, 4, 6, 8


# enumerate() - returns an enumerate object. It contains the index and value of all the items in the iterable as pairs.
# This can be useful for iteration.
# дозволяє отримувати доступ до індексу кожного елементу під час ітерації.
# одночасне отримання індексу та значення елементів ітерованого об'єкта

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

# побачите в консолі
# 0 apple
# 1 banana
# 2 cherry


# zip() - returns an iterator that combines multiple iterables into one sequence of tuples.
# використовується для одночасної ітерації по кількох колекціях

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

# побачите в консолі
# зелене яблуко
# стигла вишня
# червоний томат


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for number, letter in zip(list1, list2):
    print(number, letter)

# побачите в консолі
# 1 a, 2 b, 3 c
# zip обробляє елементи до тих пір, поки не закінчаться елементи в найкоротшій колекції


# перебирання словника

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:
    print(key)

# побачите в консолі ключі словника
# 1, 2, 3

# використовуючи метод keys, але так явно вказуємо, що хочете перебрати ключі:
for key in numbers.keys():
    print(key)

#  використористовуючи метод values, але так явно вказуємо, що хочете перебрати значення:
for val in numbers.values():
    print(val)

# побачите в консолі значення словника
# one, two, three


# Щоб перебрати пари ключ значення словника треба використати метод items.
# На кожній ітерації ми отримаємо пару (ключ, значення):
for key, value in numbers.items():
    print(key, value)

# побачите в консолі
# 1 one 2 two 3 three

# можна перезаписувати значення, якщо ви ітеруєтеся за ключами
# !!! не можна робити, поки ітеруєтеся за словником:
# !!! не можна видаляти елементи із словника,
# !!! не можна додавати елементи у словник.
