# multiline string
string = 'abc 12\
de 23 \n \tf45 6'

# matches all whitespace characters
pattern2 = '\s+'

# empty string is the separator
replace = ''

new_string = re.sub(pattern2, replace, string)
print(new_string)
