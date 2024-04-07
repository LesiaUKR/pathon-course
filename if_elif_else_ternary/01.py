# password, username
# admin and quest

username = input("Enter your username:")
password = input("Enter your password:")

if username == "admin":
    if password == "qwerty":
        print("Login successful! Welcome admin!")
    elif password == "123":
        print("Week password! Change it immediately!")
    else:
        print("Incorrect password!")
else:
    if username == "guest":
        if password == "guest_sun":
            print("Login successful! Welcome guest!")
        else:
            print("Incorrect password!")
    else:
        print("go to school")
