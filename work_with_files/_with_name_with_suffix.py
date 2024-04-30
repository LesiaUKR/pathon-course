from pathlib import Path

# Початковий шлях до файлу
original_path = Path("work_with_files/test.txt")

# Зміна імені файлу
new_path = original_path.with_name("test_one.txt")
print(new_path)

# Зміна розширення файлу
new_path = original_path.with_suffix(".md")
print(new_path)


# методи with_name і with_suffix в класі Path модуля pathlib
# в Python не змінюють фізичне ім'я файлу на диску
# original_path залишається незмінним, а new_path є новим об'єктом Path,
# який відображає шлях з новим іменем файлу.

original_path = Path("work_with_files/test_two.txt")

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("test_2.txt")

# rename - Перейменовуємо файл фізично на диску
original_path.rename(new_path)
print(original_path)
print(new_path)
