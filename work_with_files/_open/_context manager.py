# context manager - менеджер контексту
# with - автоматично закриває файл - завжди використовується на практиці
with open("work_with_files/_open/p1.jpg", "rb") as file:
    print(file.read())
    raise ValueError  # якщо виникне помилка, то файл все одно буде закритий
