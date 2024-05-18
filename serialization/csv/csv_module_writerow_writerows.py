# https://realpython.com/python-csv/
from __future__ import annotations

import csv


# DictWriter - це вбудований клас в csv, який дозволяє записувати словники в CSV-файл
with open("names.csv", "w", encoding="utf-8", newline="") as f:
   #  колонки
    fields_name = ["first_name", "last_name"]
   #  створюємо об'єкт DictWriter
    writer = csv.DictWriter(f, fieldnames=fields_name, delimiter="|")
   #  записуємо заголовок
    writer.writeheader()
   #  ключі - назви колонок, значення - дані
   # writerow - записує один рядок
    writer.writerow({"first_name": "Anastasia", "last_name": "Ivanitskaya"})
    writer.writerow({"first_name": "Yurii", "last_name": "Kuchma"})
    writer.writerow({"first_name": "Michail", "last_name": "Kravchenko"})

   #  data = [
   #      {"first_name": "Anastasia","last_name": "Ivanitskaya"},
   #      {"first_name": "Yurii", "last_name": "Kuchma"}),
   #      {"first_name": "Michail", "last_name": "Kravchenko"}
   #  ]
   #  writer.writerows(data) - записує всі рядки

with open("names.csv", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)

with open("names.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
    print(f)
