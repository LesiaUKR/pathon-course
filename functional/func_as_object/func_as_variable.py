
# Function as first class object

# Function can be saved in variable or another data structure

# function as an object criterias:
# 1. can be assigned to a variable or another data structure
# 2. pass function as an argument to another function - callback
# 3. can be returned as a result of another function


def mul(a, b):
    a = int(a)
    b = int(b)
    return a * b


def add(a, b):
    a = int(a)
    b = int(b)
    return a + b


# 1. can be assigned to a variable or another data structure
d = {
    1: mul,
    2: add
}

choice = input("Enter 1 for multiplication and 2 for addition: ")
res = add(3, 5)
print(res)

print(type(mul))  # <class 'function'>



