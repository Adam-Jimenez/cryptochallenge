import sys
import itertools
import string
from secret import generate_secret_shares


def encrypt_letter(letter, cipher):
    alphabet = string.printable
    shift = alphabet.find(cipher)
    new_alphabet = alphabet[shift:] + alphabet[:shift]
    table = bytes.maketrans(
        bytes(alphabet, 'ascii'), bytes(new_alphabet, 'ascii'))
    return letter.translate(table)

def cipher_list(plaintext, key):
    return list(zip(plaintext, itertools.cycle(key)))

def vigenere_cipher(plaintext, key):
    return ''.join([
        encrypt_letter(letter, key)
        for letter, key in cipher_list(plaintext, key)
    ])

if __name__ == "__main__":
    flag = sys.argv[1]
    secret, shares = generate_secret_shares(3,10)
    key = str(secret)
    cipher_text = vigenere_cipher(flag, key)
    with open("cipher.txt", "w") as out_file:
        out_file.write(cipher_text)
    with open("shares.txt", "w") as out_file:
        for share in shares:
            out_file.write(str(share) + "\n")
