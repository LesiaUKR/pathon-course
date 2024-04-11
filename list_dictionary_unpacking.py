# List Unpacking (розпакування списку)
my_list = [1, 2, 3]

# розпакуємо весь список
a, b, c = [1, 2, 3]
print(a)  # 1

# розпакуємо частину списку використовуючи _
a, _, c = my_list
print(c)  # 3

# розпакуємо частину списку, використовуючи *
a, *rest = my_list
print(a)  # 1
print(rest)  # [2, 3]

# Dictionary Unpacking (розпакування словника)
d = {'x': 1, 'y': 2, 'z': 3}
x, y, z = d.values()


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


person_info = {"name": "Alice", "age": 25}
greet(**person_info)
