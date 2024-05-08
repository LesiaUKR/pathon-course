def greeting_simple(name, msg):
    return f"{name} - {msg}"


print(greeting_simple("Boris", "Go to work!"))
print(greeting_simple("Boris", "Go to home!"))


def greeting(name):
    def message(msg):
        return f"{name} - {msg}"

    return message


# використовуємо, коли динамічно потрібно викликати іншу функцію
msg_for_boris = greeting("Boris")("Go to home!")  # chain of calls is currying
print(msg_for_boris)
