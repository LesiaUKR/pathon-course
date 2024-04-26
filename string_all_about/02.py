# Написати функцію, яка отримує рядок і виводить його з великої літери
# ihor -> Ihor

def capitalize(word: str) -> str:  # ihor
    # word[0] -> i
    # word[1:] -> hor
    return word.capitalize()
    # return f'{word[0].upper()}{word[1:]}'


# print('ihor'[1:4]) # word[start:end]
# print(capitalize('ihor'))