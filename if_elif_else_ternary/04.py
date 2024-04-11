# Створіть програму на Python, яка визначає категорію розробника (Junior, Middle, Senior) на основі його стажу роботи.

# Задачі:

# Отримайте від користувача стаж роботи через функцію input та збережіть це значення у змінній work_experience як ціле число.
# На основі значення work_experience вам потрібно визначити рівень розробника і зберегти це як рядок у змінній developer_type. Використовуйте наступні правила:
# Якщо стаж роботи від 1 року до 5 років включно, developer_type повинен бути "Middle".
# Якщо стаж роботи до 1 року включно, developer_type повинен бути "Junior".
# Якщо стаж роботи більше 5 років, developer_type повинен бути "Senior".

work_experience = int(input("Enter your full work experience in years: "))

if 1 < work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"
