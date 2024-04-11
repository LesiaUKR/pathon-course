is_nice = True
state = "nice" if is_nice else "not nice"

# те саме, але з використанням if-else
is_nice = True
if is_nice:
    state = "nice"
else:
    state = "not nice"


# використання тернарного оператора з or
some_data = None
msg = some_data or "Не було повернено даних"

# те саме, але з використанням if-else
some_data = None
if some_data:
    msg = some_data
else:
    msg = "Не було повернено даних"
