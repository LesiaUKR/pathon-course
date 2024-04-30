
# defaultdict - спеціальний словник, підклас dict, який входить в модуль collections.
# defaultdict приймає функцію, яка повертає значення за замовчуванням для ключів, які ще не існують в словнику.
# звичайний словник видасть KeyError, якщо ви спробуєте отримати значення для ключа, якого немає в словнику.

from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)

# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})


# defaultdict використовує int як функцію за замовчуванням,
# що означає, що кожен новий ключ має ініційоване значення 0

d = defaultdict(int)

# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1

print(d)
# defaultdict(<class 'int'>, {'a': 2, 'b': 1})

# розбити список слів на декілька списків, залежно від першої літери слова
# звичайний спосіб
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
   #  якщо ключа немає в словнику, то створюємо пустий список
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

# {'a': ['apple', 'appendix'], 'z': ['zoo'], 'l': ['lion', 'lama'], 'b': ['bear', 'bet'], 'w': ['wolf']}
print(grouped_words)

# якщо у звичаному словнику не перевірити чи існує для ключа пустий список, то буде помилка,
# бо за замовчуванням для ключа char ніякого пустого списку не існує

# використаємо defaultdict, щоб задати пустий список як значення за замовчуванням

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# використали list, але можна передати будь-яку функцію, яка викликається без аргументів.
grouped_words = defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(dict(grouped_words))

# створити словник, де ключ - це назва оператора мобільного зв'язку, а значення - список номерів телефонів
phone_numbers = [
    "0509993636",
    "0679993636",
    "0959993636",
    "0969993636",
    "0509993637",
    "0639993636",
    "0509993632",
    "0339993632",
]

phone_operator_numbers = defaultdict(list)

for ph in phone_numbers:
    if ph.startswith("050") or ph.startswith("095"):
        phone_operator_numbers["Vodafone"].append(
            ph
        )  # since by default value is list, you can call .append
    elif ph.startswith("067") or ph.startswith("096"):
        phone_operator_numbers["Kyivstar"].append(ph)
    elif ph.startswith("063") or ph.startswith("093"):
        phone_operator_numbers["Lifeceil"].append(ph)
    else:
        phone_operator_numbers["Unknown"].append(ph)

print(phone_operator_numbers)
