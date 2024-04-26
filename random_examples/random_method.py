import random

# генерує випадкове ціле число від 1 до 1000 - N таке, що a <= N <= b:
random.randint(1, 1000)

# наприклад, підходить для симуляції кидка кубика:
dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")


# random.random() потрібен, щоб отримати випадкове число в інтервалі 0, 1.
# Він генерує випадкове дійсне число між 0.0 (включно) та 1.0 (не включно):

num = random.random()
print(num)  # виведе випадкове число в інтервалі 0, 1

# симулювати випадкове відсоткове заповнення
fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%")

# форматування {fill_percentage:.2f} яке вказує, яким чином відображати змінну fill_percentage.
# Вираз .2 це кількість знаків після десяткової крапки. У цьому випадку вказано,
# що потрібно відображати два знаки для дійсного числа. Символ f означає,
# що число має бути відображене у форматі дійсного числа.


# random.randrange(start, stop[, step]) - повертає випадково вибране число з заданого діапазону.
# Параметри методу:

# start - нижня межа діапазону (включно). Це початкове значення,
# з якого може починатися випадковий вибір.
# Якщо не вказано, за замовчуванням приймається нуль, і діапазон починається з 0.
# stop - верхня межа діапазону (не включно). Це означає, що вибране випадкове
# число буде меншим, ніж це значення.
# Цей параметр є обов'язковим, і метод не буде працювати без нього.
# step - крок між можливими значеннями. Наприклад, якщо встановити step як 2,
# метод буде вибирати лише парні числа або числа, кратні 2,
# в залежності від start. Цей параметр є необов'язковим і за замовчуванням дорівнює 1,
# що означає, що вибір відбувається з усіх послідовних чисел у діапазоні.

# обирає випадкове число від 0 до 9
print(random.randrange(10))  # Верхня межа є 10, але не включається

# симуляція пострілу по мішені, але необхідно вибрати випадковий
# номер від 1 до 10, та лише непарні числа:

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

# random.shuffle(x) - Коли у вас є список об'єктів і вам потрібно перемішати
# порядок елементів в цьому списку на випадковий, де x - список, який потрібно перемішати.

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)

print(f"Перемішана колода: {cards}")

# random.choice(seq)- Якщо потрібно вибрати випадковий елемент зі списку,
# де seq - послідовність для вибору: список або кортеж.

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))  # виведе випадковий фрукт

# random.choices() - Щоб вибрати більше чим один випадковий елемент зі списку
# Синтаксис методу random.choices() наступний:

# random.choices(population, weights=None, cum_weights=None, k=1)

# population - послідовність список, з якої має бути зроблений вибір.
# weights - опціональний список, який вказує ймовірності (ваги)
# кожного елемента в списку population. Ці ваги визначають,
# наскільки ймовірно, що конкретний елемент буде обраний.
# Довжина списку weights має бути дорівнювати довжині списку population.
# cum_weights - теж опціональний список кумулятивних ваг.
# Якщо він вказаний, то список weights ігнорується.
# Кумулятивна вага кожного елемента визначається
# як сума його ваги плюс ваги всіх попередніх елементів.
# k: Кількість елементів для вибору. За замовчуванням k=1.

# Вибирає один фрукт зі списку:
items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item)

# Вибір декількох елементів з можливістю повторень:
numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)


# Вибір з вагами:
colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)

# random.sample(population, k) - Якщо виникає необхідність вибрати N елементів зі списку
# і вони при цьому не повторювалися
# повертає список довжиною k з унікальними елементами, вибраними випадково з population.
# k не може бути більше довжини participants


participants = ['Анна', 'Богдан', 'Віктор', 'Галина',
                'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")

# random.uniform(a, b)- Метод повертає випадкове дійсне число N, таке що a <= N <= b.

# Приклад генерації випадкової ціни для продукту в межах від 50 до 100:

price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")