import re
from collections import defaultdict

country_codes_dict = {
    '+38': 'UKR',
    '+12': 'USA',
    '+44': 'GBR',
    '+61': 'AUS',
    '+49': 'GER'
}

# +1(234)567-8-901
# +12345678901


def sanitize_phone_number(number: str) -> str:
    return re.sub(r'[()\-]', '', number)

#  defaultdict(list) - значення за замовчуванням для кожного ключа - пустий список
# можна передавати в set, list, dict
# defaultdict - це підклас dict, який автоматично створює значення для нових ключів
# , він автоматично створює новий список\множину\словник для кожного нового ключа, якщо такого ключа раніше не існувало.


def split_numbers_by_countries(phone_numbers: list[str]) -> dict[str, list]:
    # задаємо значення за замовчуванням для кожного ключа - пустий список
    countries_dict = defaultdict(list)
    for phone_number in phone_numbers:
        phone_number = sanitize_phone_number(phone_number)
        prefix = phone_number[:3]
        key = country_codes_dict.get(prefix)  # 'UA', 'USA',..., None ('Other')
        countries_dict[key].append(phone_number)
    return countries_dict


# +380(67)777-7-777
# USA: +1(234)567-8-901
# UK: +44(123)456-7-890
# Australia: +61(234)567-8-901
# Germany: +49(123)456-7-890
# ['+380(67)777-7-777', '+1(234)567-8-901', '+44(123)456-7-890', '+61(234)567-8-901', '+1(234)567-8-901']

# result_dict = {'USA': ['+1(234)567-8-901'], 'UK': ['+44(123)456-7-890']}
# result_dict = {'USA': ['+12345678901'], 'UK': ['+441234567890']}

# countries_dict = defaultdict(list)
# # countries_dict = dict() # на відміну від defaultdict видасть помилку, бо не можна додавати значення до неіснуючого ключа
# print(countries_dict)
# countries_dict['URK'].append('1234567890')
# print(countries_dict)
print(sanitize_phone_number('+1(234)567-8-901'))

result = split_numbers_by_countries(['+380(67)777-7-777', '+1(234)567-8-901',
                                    '+44(123)456-7-890', '+61(234)567-8-901', '+1(234)567-8-901', '+49(123)456-7-890'])
for country_code, phone_numbers in result.items():
    print(f'{country_code}: {phone_numbers}')
