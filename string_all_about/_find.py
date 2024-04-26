# chrome-extension://gphandlahdpffmccakmbngmbjnjiiahp/https://math.asu.edu/sites/default/files/affine.pdf
# https://en.wikipedia.org/wiki/Affine_cipher

def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the alphabet
            # % len(alpha) to return to the beginning of the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)
            print(letter_index)
            result = result + alpha[letter_index]
            print(result)
        else:
            result = result + letter

    return result


# DTWVG KU IQQPC MKN OG - encrypted message
res = encrypt(2, "Brute is gonna kill me")
# BRUTE IS GONNA KILL ME - decrypted message
res = encrypt(-2, "DTWVG KU IQQPC MKN OG")
print(res)
