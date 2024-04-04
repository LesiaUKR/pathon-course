def hello(name):  # name - параметр
    print("Hello there", name)
    print("Hi there", name)


print("Hello out of there")  # відобразиться першим, бо викликається першим

hello("Kate")  # Kate - аргумент
hello("Oleh")


def sum_nums(a, b):
    sum = a + b
    return sum


sum_nums(10, 20)
