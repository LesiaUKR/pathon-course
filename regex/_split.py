import re

# task 1
string = "Twelve:12 Eighty nine:89."
pattern1 = "\\d+"

result = re.split(pattern1, string)
print(result)

result = re.split(pattern1, string, maxsplit=1)
print(result)


# task 2

# multiline string
string = 'abc 12\
de 23 \n \tf45 6'

# matches all whitespace characters
# SyntaxWarning: invalid escape sequence '\s'  - це попередження, що потрібно використовувати екранування
pattern2 = '\\s+'


# empty string
replace = ''

new_string = re.sub(pattern2, replace, string)
print(new_string)  # Output: abc12de23f456

# повертає кортеж з двома значеннями - новий рядок і кількість замінених символів
new_string = re.subn(pattern2, replace, string)
print(new_string)  # Output: ('abc12de23f456', 4)
