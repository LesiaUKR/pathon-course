print("Hello Python")
# help(print) - виведе документацію по переданій функції print
# print(print)

# input буде просити щось користувача ввести із клавіатури в терміналі
# name=input("Enter your name")

# значення, яке користувач вводить після виклику функції input це завжди строка
# якщо потрібен інший вид значення, його потрібно буде конвертувати
# print(name)

# dir покаже імена всіх атрибутів(методів), які доступні об'єкту name
# все це можливо, бо в python все є об'єктами, які наслідують методи від классів з яких вони були створені
newName = "Lesia"
# print(dir(name))

# якщо нічого не вказати в dir, вона покаже список
print(dir())

# викликаємо методи через точкову нотацію
name = "lesia"
print(dir(name))
print(name)
print(name.rfind("n"))
print(name.capitalize())


print(10, "None", True)

my_list = [1, 2, 3]
print(my_list)
