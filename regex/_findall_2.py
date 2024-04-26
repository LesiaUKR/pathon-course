import re
# find max vowels chain in a string

#


def find_max_vowels(text):
    r = r"[aeiou]+"
    chains = re.findall(r, text)
    res = max(chains, key=len)
    return res, len(res)
   #  return max(re.findall(r"[aeiou]+", text), key=len, default="")


text = "aevsaefsdsade asds d asd sa  Oleeeeeeeeh"
res = find_max_vowels(text)

print(res)
