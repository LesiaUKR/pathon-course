from __future__ import annotations

import csv

country_codes = {}

with open("countries.csv", "r") as f:
   #  DictReader - використовується, коли є назви колонок в CSV-файлі
   # DictReader - читає рядки як словники, тобто ключі - назви колонок, значення - дані
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
   #  reader = csv.reader(f)
   #  header = next(reader)
   #  for line in reader:
   #      country_codes[line[0]] = line[1]

# print(country_codes)
# print(country_codes["UA"])
