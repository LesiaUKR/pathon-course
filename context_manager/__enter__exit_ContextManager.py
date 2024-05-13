class MyContextManager:
    def __enter__(self):
        # Ініціалізація ресурсу
        print("Enter the block")
        return self  # Може повертати об'єкт

    def __exit__(self, exc_type, exc_value, traceback):
        # Звільнення ресурсу
        print("Exit the block")
        if exc_type:
            print(f"Error detected: {exc_value}")
        # Повернення False передає виключення далі, True - поглинає виключення.
        return False


# Використання власного менеджера контексту
with MyContextManager() as my_resource:
    print("Inside the block")
    raise Exception("Something went wrong")

# Якщо блок with завершився без помилки, то значення змінних exc_type, exc_val, exc_tb дорівнюють None
# def __exit__(self, exc_type, exc_val, exc_tb):
#     # Звільнення ресурсів
#     # exc_type: тип виключення
#     # exc_val: значення виключення
#     # exc_tb: трасування стека виключення
#     return False  # Якщо True, виключення буде придушено, інакше - прокинуто далі
