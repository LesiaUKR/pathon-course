text5 = "Контакти: example1@example.com, example2@sample.org"
pattern7 = r"\w+@\w+\.\w+"
matches = re.findall(pattern7, text5)

print(matches)  # Виведе всі знайдені електронні адреси