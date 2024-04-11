# Напишіть функцію format_string, яка центрує рядок у рамках заданої
# довжини length.

# Задачі:

# Створіть функцію format_string, яка приймає два аргументи:
# string рядок, який потрібно форматувати та length довжина,
# у межах якої потрібно центрувати рядок.
# Якщо довжина string більша або дорівнює length, поверніть
# рядок без змін.
# Якщо довжина string менша за length, додайте перед рядком
# пробіли, для того, щоб рядок був центрований у рамках length.
# Кількість пробілів визначте за формулою (length - len(string)) // 2.
# Поверніть з функції відформатований рядок, що центрується у межах
# length. Очікуваний результат:

# Функція format_string повертає відформатований рядок відповідно
# до заданих правил.

# Підказки:
# Використовуйте len() для визначення довжини рядка.
# Для створення рядка з пробілів використовуйте " " * кількість_пробілів.


def format_string(string, length):
    gaps = (length - len(string)) // 2
    gap_string = " " * gaps
    print(gaps)
    print(gap_string)
    if len(string) >= length:
        return string
    else:
        return f"{gap_string}{string}{gap_string}"


print(format_string("Hello", 10))  # "  Hello  "
print(format_string("abaa", 15))  # "     abaa     "
