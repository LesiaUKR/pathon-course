import re

# re.search(pattern, string, flags=0) — повертає спеціальний об'єкт Match,
# якщо шаблон було знайдено в рядку, інакше None
# pattern: Регулярний вираз (шаблон), який ви хочете знайти.
# string: Рядок, у якому ви хочете знайти шаблон.

# Match.span() повертає кортеж, що містить початкову та кінцеву позиції збігу.
# Match.string повертає рядок, переданий у функцію,
# Match.group() повертає частину рядка, в якому був збіг


# pattern означає, що рядок має починатися з 'a' та закінчуватися на 's'
pattern = "^a.+s$"
test_string = "abyss"
result = re.match(pattern, test_string)
res = re.search(pattern, test_string)
print(result)  # Match - match повертає об'єкт Match і шукає з початку рядка
print(res)  # search - search повертає об'єкт Match і шукає по всьому рядку

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")


# різниця між match та search
claim = "People love Python."

print(re.search(r"Python", claim))
# => Python

print(re.match(r"Python", claim))
# => None

print(re.search(r"People", claim))
# => People

print(re.search(r"People", claim))
# => People
