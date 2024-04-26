import re

string = "39802 356, 2102 1111"

# Three digit number followed by space followed by two digit number
pattern = r"(\d{3}) (\d{2})"
# [] - перелік 

# match variable contains a Match object.
result = re.search(pattern, string)

# capturing groups - (\d{3}) \ non-capturing groups - (?\d{3})

print(result.group())  # 802 35 -
print(result.groups())  # ('802', '35') -

# if match:
#     print(match.group())
# else:
#     print("pattern not found")


# print(match.group(1))
# print(match.group(2))
# print(match.start())
# print(match.end())
