import csv

# Дані для запису
rows = [
    ["name", "age", "specialty"],
    ["Василь Гупало", 30, "Математика"],
    ["Марія Петренко", 22, "Фізика"],
    ["Олександр Коваленко", 20, "Інформатика"],
]

file_name = "data.csv"

# Відкриваємо файл для запису
with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
    # Створюємо об'єкт writer
    writer = csv.writer(csvfile, delimiter=",")
    # Записуємо рядки даних
    writer.writerows(rows)
