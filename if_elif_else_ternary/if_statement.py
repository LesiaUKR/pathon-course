age = int(input("What is your age: "))

if age >= 18:
    print("You can drink alcohol!")
else:
    print("Go to school my friend!")


if age == 17:
    print("You almoost can drink alcohol!")
elif age == 18:
    print("You are old now!")
else:
    print("Go to school my friend!")

# аналог switch case в інших мовах програмування
if age == 18:
    print("You are old now!")
elif age == 18:
    print("You are old now!")
elif age == 19:
    print("You are old now!")
elif age == 20:
    print("You are old now!")
else:
    print("Go to school my friend!")

# ternary operator
# <condition true> if <condition> else <condition false>
print("You can drink alcohol!") if age >= 18 else print(
    "Go to school my friend!")
