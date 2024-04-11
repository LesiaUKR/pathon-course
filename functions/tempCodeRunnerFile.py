def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    number_of_groups=factorial(n) / (factorial(n - k) * factorial(k))
    print(int(number_of_groups))
    return int(number_of_groups)

number_of_groups(50, 7)