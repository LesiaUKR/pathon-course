# Метод send() використовується для взаємодії з генератором
# шляхом надсилання значення у генератор,
# яке потім може бути використане як результат виразу yield

def my_generator():
    received = yield "Ready"
    yield f"Received: {received}"


gen = my_generator()
print(next(gen))
print(gen.send("Hello"))
