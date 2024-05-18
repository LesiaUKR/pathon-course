# __add__(self, other) для оператора +
# __sub__(self, other) для оператора -
# __mul__(self, other) для оператора *
# __truediv__(self, other) для оператора /
# __floordiv__(self, other) для оператора цілочисельного ділення //
# __mod__(self, other) для оператора залишку від ділення %
# __pow__(self, other) для оператора * піднесення до степеня


from collections import UserDict


class MyDict(UserDict):
    def __add__(self, other):
        temp_dict = self.data.copy()
        temp_dict.update(other)
        return MyDict(temp_dict)

    def __sub__(self, other):
        temp_dict = self.data.copy()
        for key in other:
            if key in temp_dict:
                temp_dict.pop(key)
        return MyDict(temp_dict)


if __name__ == '__main__':
    d1 = MyDict({1: 'a', 2: 'b'})
    d2 = MyDict({3: 'c', 4: 'd'})

    d3 = d1 + d2
    print(d3)

    d4 = d3 - d2
    print(d4)
