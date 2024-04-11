# Оператор match
# оператор match - це новий спосіб заміни оператора switch з Python 3.10
# Структура оператора match

# match змінна:
#     case шаблон1:
#         # виконати код для шаблону 1
#     case шаблон2:
#         # виконати код для шаблону 2
#     case _:
#         # виконати код, якщо не знайдено відповідностей

#  якщо жоден з варіантів не відповідає значенням case
# (тобто fruit не є ні "apple", ні "banana", ні "orange"),
# то виконується блок коду під case _

# Приклад
fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")

# використання оператора match для порівняння координат точки
point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}")
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}")
    case _:
        print("Це не точка")

# оператор match з колекціями
pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")
