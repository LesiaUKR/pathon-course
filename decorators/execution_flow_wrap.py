from functools import wraps

# wraps  - декоратор, який копіює атрибути функції, яку декоруємо


def star(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__)
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)

    return inner


def percent(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)

    return inner


@percent
@star
def printer(msg):
    print(msg)


printer("Мабуть у стовпчик одна над іншою")
# __wrapped__ - знімаємо декоратори знизу вгору
printer.__wrapped__("Мабуть у стовпчик одна над іншою")
# без жодного декоратора
printer.__wrapped__.__wrapped__("Мабуть у стовпчик одна над іншою")
# print(dir(printer))
