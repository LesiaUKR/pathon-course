import math

a = int(input("Enter a side length: "))
b = int(input("Enter a side length: "))
c = int(input("Enter a side length: "))
print(a, b, c)

P = a + b + c

p = P / 2

S = math.sqrt(p * (p-a) * (p-b) * (p-c))

print("Square is", S)
print("Square is {}".format(S))  # format робить те ж саме що і f-string
print(f"Square is {S}")
