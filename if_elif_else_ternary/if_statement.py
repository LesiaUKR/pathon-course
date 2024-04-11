age = int(input("What is your age: "))

if age >= 18:
    print("You can drink alcohol!")
else:
    print("Go to school my friend!")


if age == 17:
    print("You almoost can drink alcohol!")
elif age == 18:
    print("You are old now!")
else:
    print("Go to school my friend!")

# аналог switch case в інших мовах програмування
if age == 18:
    print("You are old now!")
elif age == 18:
    print("You are old now!")
elif age == 19:
    print("You are old now!")
elif age == 20:
    print("You are old now!")
else:
    print("Go to school my friend!")

# ternary operator
# <condition true> if <condition> else <condition false>
print("You can drink alcohol!") if age >= 18 else print(
    "Go to school my friend!")

# число 0 приводиться до False
money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")


# значення None приводиться до False
result = None
if result:
    print(result)
else:
    print("Result is None, do something")

# порожній контейнер, порожній рядок тощо, приводиться до False
user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")

# Логічні операції
# Задача "FizzBuzz"
# Виводить "Fizz", якщо число кратне якомусь певному числу (наприклад, 3);
# Виводить "Buzz", якщо число кратне іншому певному числу (наприклад, 5);
# Виводить "FizzBuzz", якщо число кратне обом цим числам;
# В іншому випадку виводить саме число.

# Задаємо конкретне число
num = int(input("Enter a number:"))

# Перевіряємо кратність
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")
