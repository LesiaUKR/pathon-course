from time import time, sleep


def measure(func):
    def wrapper(*args, **kwargs):

      #   print("Before function is called")
        t = time()
        res = func(*args, **kwargs)
      #   func.__name__ - дозволяє повернути ім'я функції, яку обгорнули
        print(func.__name__, "took", time() - t)

      #   print("After function is called")
        return res

    return wrapper


@measure
def sleepy_function(sleep_time):
    sleep(sleep_time)
    print("I'm done")
    return "OK"

# вимірюємо час виконання функції
# це незручно, тому використовуємо декоратор measure
# start = time()
# sleepy_function(3)
# end = time()
# print("Elapsed time", end - start)


print(sleepy_function(0.3))
sleepy_function(0.5)

# декоратор можна використовувати для вимірювання часу виконання будь-якої функції


@measure
def is_unique(checklist):
    return len(checklist) == len(set(checklist))


is_unique([1, 2, 3, 4, 5, 1, 5])
