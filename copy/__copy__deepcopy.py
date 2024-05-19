from copy import copy, deepcopy
from collections import UserList

# на прпктиці використовується deepcopy, а не магічні методи
# __copy__ і __deepcopy__ викликаються при використанні copy() і deepcopy()
# prototype pattern - і сам об'єкт говорить, як його копіювати


class CopyList(UserList):
    def __copy__(self):
        print("Copy magic method is called")

    def __deepcopy__(self, memodict={}):
        print("Deep Copy magic method is called")


l = CopyList([1, 3, ['a', 'b', 'c']])
print(l)

l2 = deepcopy(l)
