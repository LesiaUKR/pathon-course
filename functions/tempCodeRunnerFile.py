def closure():
    count = 0

    def add(n):
        nonlocal count
        count += n
        return count
    return add


my_add = closure()  # повернення функції add
print(my_add(5))

my_second_add = my_add
print(my_second_add(2))