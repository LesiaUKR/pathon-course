import random
import re
import string

# import string - модуль, який містить корисні константи та класи для роботи з рядками

source = "abcdefghijklmnopqrstuvwxyz"
# (string.punctuation) # перелік всіх спеціальних символів - !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
password_symbols = f'A-Za-z0-9{string.punctuation}'
password_regexp = r"[" + password_symbols + "]{8,}"
# password_regexp = r"[\w]{8,}"

# Password: minimum 8 symbols and minimum one special symbol


def check_password(password: str) -> bool:
    if not re.search(password_regexp, password):
        return False
    return True


# ord chr - перетворення символів в числа та навпаки за таблицею ASCII
# for position in range(ord('a'), ord('z') + 1):
#     print(chr(position), end='') # виведе алфавіт від a до z в один рядок за допомогою end=''

# "baad"
# функція ord() повертає рандомне числове представлення символу
def get_random_value() -> str:
    return chr(random.randint(33, 126))


def random_password(n: int) -> str:
    password = ""
    for _ in range(n):  # _ - змінна, яка не використовується, коли нам просто потрібно виконати певну кількість ітерацій
        password += get_random_value()
    return password


my_password = random_password(8)
print(my_password)
print('Password is correct:', check_password(my_password))
# print(string.punctuation) # перелік всіх спеціальних символів - !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
