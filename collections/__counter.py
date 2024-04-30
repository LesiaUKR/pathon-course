from collections import Counter

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)  # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}


# most_common() - повертає список з n найбільш часто зустрічаючимися елементами та їх кількістю
# most_common() - це метод класу Counter із модуля collections
# most_common() - повертає список кортежів, де перший елемент кортежу - це елемент, а другий - його кількість

# str, list, tuple - ітерабельні об'єкти, які можна передати у Counter
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = Counter(student_marks)


# [(4, 4), (6, 3), (7, 2), (2, 2), (3, 2), (5, 2), (1, 3)]
print(mark_counts.most_common())
print(mark_counts.most_common(1))  # [(4, 4)]
print(mark_counts.most_common(2))  # [(4, 4), (6, 3)]


# Створення Counter з рядка
letter_count = Counter("banana")
print(letter_count)
# Counter({'a': 3, 'n': 2, 'b': 1})

# Виконати підрахунок слів в тексті
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")

# the: 2
# quick: 1
# brown: 1
# fox: 1
# jumps: 1
# over: 1
# lazy: 1
# dog: 1

# За допомогою Counter можна перевірити, чи є слова анаграмами

# anagram when "oleh" == "helo" - мають однакові літери в однаковій кількості


def is_anagram(word1, word2):
    """Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    return Counter(word1) == Counter(word2)


res = is_anagram("asds", "sads")
print(res)

# звичайний спосіб
