# Path.unlink(missing_ok=False)
# Параметр missing_ok якщо має значення True,
# то виключення не буде викинуто, якщо файл не існує.
# За замовчуванням False, це означає, що буде викинуто
# виняток FileNotFoundError, якщо файл не існує.

from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')

# видалення файлу без попередньої перевірки його існування, використовуючи параметр missing_ok
# виключення не буде викинуто

file_path = Path('/path/to/file.txt')
file_path.unlink(missing_ok=True)
