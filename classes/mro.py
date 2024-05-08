# Description: Method Resolution Order (MRO) - порядок розгляду класів при спадкуванні

class A:
    x = "a"


class B(A):
    x = "b"


class C(A):
    x = "c"


class D(B, C):
    def get_x(self):
        return D.x


# вбудована функція __mro__ визначає порядок розгляду класів при спадкуванні
print(D.__mro__)  # виведе порядок розгляду класів при спадкуванні (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.mro())  # поверне список класів, які будуть розглядатися при спадкуванні

d = D()
print(d.x)  # b - спочатку шукає в класі D, потім в B, бо B перший в списку наслідування
d.get_x()
