
def greeting(name):
    def message(msg):
        return f"{name} - {msg}"

    return message


msg_for_boris = greeting("Boris")
msg_for_kirill = greeting("Kirill")

print(msg_for_boris("Go to home!"))
print(msg_for_boris("Go to work!"))