def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError as e:
            print(f"Error happened, can not divide by zero: {e}")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            # raise  # re-throw the last exception

    return wrapper


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@log_errors
def divide(x, y):
    return x / y


res = divide(1, 1)
print(res)
