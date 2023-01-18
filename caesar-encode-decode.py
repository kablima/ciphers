import string

alphabet = string.ascii_lowercase
punctuation = ".;,?'! "

def encode(my_mess, offset):
    encoded = ""
    for letra in my_mess:
        if not letra in punctuation:
            valor = alphabet.find(letra)
            encoded += alphabet[(valor - offset) % 26]
        else:
            encoded += letra
    return encoded

def decode(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message

print(encode('i like coding and cryptography', 8))
# a dacw ugvafy sfv ujqhlgyjshzq

print(decode('a dacw ugvafy sfv ujqhlgyjshzq', 8))
# i like coding and cryptography