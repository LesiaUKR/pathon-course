from __future__ import annotations

import csv

country_codes = {}

# reader  - зчитує рядки як список, а не словник
with open("countries.csv", "r") as f:
    reader = csv.reader(f)
   #  скіпаємо перший рядок
    header = next(reader)
    for line in reader:
        country_codes[line[0]] = line[1]

print(country_codes)
print(country_codes["UA"])
