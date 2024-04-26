
import re


def replace_rule(spam_word):
    return "*" * (len(spam_word.group()))

#    pattern = r"(idiot|coder)" - r - це прямо сказати, що це регулярний вираз


def replace_bad_words(text, bad_words):
    pattern = r"(idiot|coder|be)"
   #  return re.sub(pattern, "**", text)
    return re.sub(pattern, replace_rule, text)
   #  return re.sub(pattern, replace_rule, text, flags=re.IGNORECASE) - регістронезалежний пошук


text = "to be or not to be an idiot. BE a good coder!"
censored_text = replace_bad_words(text, ["idiot", "coder"])
print(censored_text)


# REGEX = compile(r",+")


# def dad_filter(strng):
#     return sub(REGEX, ",", strng).rstrip(" ,")


# res = dad_filter("asdsad,d,as,dsa,dsa,das,d,,,asdsad ,,,asd,,")
# print(res)
