def hello(name):  # name - параметр
    print("Hello there", name)
    print("Hi there", name)


print("Hello out of there")  # відобразиться першим, бо викликається першим

hello("Kate")  # Kate - аргумент
hello("Oleh")


def sum_nums(a, b):
    sum = a + b
    return sum

# якщо функція має return, то її виклик потрібно присвоїти змінній
# якщо функція не має return, то вона повертає None


first_sum = sum_nums(10, 20)
print(first_sum)
print(sum_nums(50.5, 20))
print(sum_nums(10, 20) + 30)
print(sum_nums(sum_nums(10, 20), 30))

print(print("Hello"))  # завжди виводить None, бо print не має return
