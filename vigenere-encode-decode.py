import string

alphabet = string.ascii_lowercase
punctuation = ".,?'! "

def vigenere_coder(original_message, keyword):
    letter_pointer = 0
    keyword_final = ""
    for i in range(len(original_message)):
        if original_message[i] in punctuation:
            keyword_final += original_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)

    encoded_message = ""
    for i in range(len(original_message)):
        if original_message[i] in punctuation:
            encoded_message += original_message[i]
        else:
            value_1 = alphabet.find(original_message[i])
            value_2 = alphabet.find(keyword_final[i])
            encoded_message += alphabet[(value_1-value_2)%26]
    return encoded_message

def vigenere_decode(encoded_message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(len(encoded_message)):
        if encoded_message[i] in punctuation:
            keyword_final += encoded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    
    decoded_message = ""
    for i in range(len(encoded_message)):
        if encoded_message[i] in punctuation:
            decoded_message += encoded_message[i]
        else:
            value_1 = alphabet.find(encoded_message[i])
            value_2 = alphabet.find(keyword_final[i])
            decoded_message += alphabet[(value_1+value_2)%26]
    return decoded_message

print(vigenere_coder("let's write some code", "python"))
# wga'l ietvl lazp evwq

print(vigenere_decode("ek'em mbqtt bu gpk zwua!", "sun"))
# we're going to the moon