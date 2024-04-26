# Написати функцію, яка отримає речення та виведе слова у реченні у зрототньому порядку
# 'Hello world, hello people!' -> 'People hello world hello'

def clean_extra_symbols(sentence: str) -> str:
    # return sentence.replace(',' or '!' or '.', '')
    return sentence.replace(',', '').replace('!', '').replace('.', '')


# print(clean_extra_symbols('Hello world, hello people!'))


def reverse_words_in_sentence(sentence: str) -> str:
    # Прибрати знаки
    cleaned_sentence = clean_extra_symbols(sentence)
    # Розділити речення на окремі слова
    # 'Hello world, hello people!' -> ['Hello', 'world,', 'hello', 'people!']
    words_list = cleaned_sentence.split()
    # Змінити порядок слів у зворотньому порядку
    words_list = words_list[::-1]
    # Зробити перше слово з великої, старе перше з малої
    # [1, 2, 3]
    # lst[2] = 4
    words_list[-1] = words_list[-1].lower()
    words_list[0] = words_list[0].capitalize()
    return ' '.join(words_list)


print(reverse_words_in_sentence('Hello world, hello people!'))
