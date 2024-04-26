# isdigit() - метод, який перевіряє, чи складається рядок лише з цифр
# isnumeric() - метод, який перевіряє, чи складається рядок лише з чисел
# різниця між isdigit() та isnumeric() в тому, що isnumeric() визнає символи,
# які не є цифрами, але є числами, наприклад, дробові числа, числа у формі дробу,
#  числа у формі індексу, числа у формі римських чисел тощо.

mystr = '12345'
print(mystr.isdigit())

mystr = '10.5'
print(mystr.isdigit())

mystr = 'python'
print(mystr.isdigit())


pay_system = {5: "MasterCard", 4: "Visa", 3: "American Express"}

card_number = ["5375414112345678", "4168757587879876", "216875758787987d"]


def isvalid_card(card):
    # ^[0-9]{16}$
    return card.isdigit() and len(card) == 16

# перевірка чи це число


def is_float(string):
   #  return string.replace(".", "").isdigit()
    # або через if else робимо перевірку
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False


print(is_float('1.23'))  # True
print(is_float('123'))  # True
print(is_float('1.23a'))  # False

# ще один спосіб перевірки на число


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


print(is_float('1.23'))
print(is_float('123'))
print(is_float('1.23a'))
