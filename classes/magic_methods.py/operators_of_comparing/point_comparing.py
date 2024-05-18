# __eq__(self, other) — визначає поведінку під час перевірки на відповідність ( == ).
# __ne__(self, other) — визначає поведінку під час перевірки на невідповідність. != .
# __lt__(self, other) — визначає поведінку під час перевірки на менше < .
# __gt__(self, other) — визначає поведінку під час перевірки на більше > .
# __le__(self, other) — визначає поведінку під час перевірки на менше-дорівнює <= .
# __ge__(self, other) — визначає поведінку під час перевірки на більше-дорівнює >= .


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x >= other.x and self.y >= other.y


if __name__ == "__main__":
    print(Point(0, 0) == Point(0, 0))  # True
    print(Point(0, 0) != Point(0, 0))  # False
    print(Point(0, 0) < Point(1, 0))  # False
    print(Point(0, 0) > Point(0, 1))  # False
    print(Point(0, 2) >= Point(0, 1))  # True
    print(Point(0, 0) <= Point(0, 0))  # True
