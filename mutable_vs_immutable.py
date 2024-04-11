# mutable data types: list, set, dictionary, bytearray, array
# можна змінювати
# швидше працюють при записі в пам'ять
# при переборі - працює повільніше
# не має фіксованого розміру

# immutable data types: integers, floating-point numbers, boolean, string, tuple, frozenset, bytes
# не можуть бути змінені після їх створення
# швидше модифікувати
# швидше працює при зчитуванні з пам'яті
# має фіксований розмір

# У Python всі об'єкти передаються за посиланням
# Коли незмінний об'єкт передається у функцію,
# фактично передається його копія, і будь-які зміни
# цього об'єкту в функції не впливають на оригінальний об'єкт.

def modify_string(original: str) -> str:
    original = "змінено"
    return original


str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)                # виведе: оригінал


# Коли змінний об'єкт передається у функцію,
# передається посилання на об'єкт, а не його копія.

def modify_list(lst: list) -> None:
    lst.append(4)


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]


# Використовуйте метод copy() для створення копій змінних об'єктів,
# якщо не хочете змінювати оригінал.

def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]

# список my_list після виконання функції modify_list вже не зазнає змін

# задача: конвертувати кожен символ у рядку в його відповідний код ASCII.


def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}
    # Перебір кожного символу в рядку
    for ch in string:
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник
            codes[ch] = ord(ch)
    return codes


result = string_to_codes("Hello world!")
print(result)
