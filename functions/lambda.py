from time import time_ns

# first variant


def cubed(x):
    return x ** 3

# second variant


def lambda_cubed(x): return x ** 3


start = time_ns()
print(f"Cube of 9 is {cubed(9)}")
print(f"Time taken for previous method: {(time_ns() - start)//1_000} ms")


start = time_ns()
print(f"Cube of 9 is {lambda_cubed(9)}")
print(f"Time taken for lambda method: {(time_ns() - start)//1_000} ms")

# 3 variant
start = time_ns()
print(f"Cube of 9 is {(lambda x: x**3)(9)}")
print(f"Time taken for inline lambda : {(time_ns()-start)//1_000} ms")


# what is faster? lambda or function?


# функція лямбда, яка нічого не повертає
def cube():
    print("Hello")

# lambda функція, яка нічого не повертає


def lambda_cubed():
    return print("Hello")


def lambda_cubed(): return print("Hello")


lambda_cubed()

print(cube())
