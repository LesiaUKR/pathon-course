# store all vowels "aeiou"


# https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/python
def longest_word(string_of_words):
    words = string_of_words.split()
    res = words[0]
    for word in words:
        if len(word) >= len(res):
            res = word
    return res


# find max vowels chain in a string
def find_max_vowels(text):
    vowels = "aeiou"
    # replace consonant with dot .
    for character in text:
        if character.lower() not in vowels:
            # ae..ae....a.e a......a....a..O.eeeeeeee.
            text = text.replace(character, ".")

   # split by dot
    chains = text.split(".")
   #  res = max(chains, key=len) - the same as below but with another way
   #  sort by length
    chains.sort(key=len)
   #  get the longest chain
    max_chain = chains[-1]
    return max_chain, len(max_chain)


text = "aevsaefsdsade asds d asd sa  Oleeeeeeeeh"
res = find_max_vowels(text)

print(res)
