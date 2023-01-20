import string

alphabet = string.ascii_lowercase
print(alphabet)
punctuation = ".;,?'! "

def caesar_brute_force(my_mess):
    for i in range(1, 25):
        encoded = ""
        for letra in my_mess:
            if not letra in punctuation:
                valor = alphabet.find(letra)
                encoded += alphabet[(valor - i) % 26]
            else:
                encoded += letra
        print("Offset is " + str(i) + ": " + encoded)
    return None

print(caesar_brute_force('sahykia pk iu cepdqx'))
# secret message is: 'welcome to my github'.