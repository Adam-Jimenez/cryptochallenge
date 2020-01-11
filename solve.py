import shamir
import itertools
import string
from ast import literal_eval as make_tuple

def encrypt_letter(letter, cipher):
    alphabet = string.printable
    shift = alphabet.find(cipher)
    new_alphabet = alphabet[shift:] + alphabet[:shift]
    table = bytes.maketrans(
        bytes(new_alphabet, 'ascii'), bytes(alphabet, 'ascii'))
    return letter.translate(table)

def cipher_list(plaintext, key):
    return list(zip(plaintext, itertools.cycle(key)))

def vigenere_cipher(plaintext, key):
    return ''.join([
        encrypt_letter(letter, key)
        for letter, key in cipher_list(plaintext, key)
    ])

if __name__ == "__main__":
    shares = []
    cipher = open("cipher.txt").read().strip()
    with open("shares.txt", "r") as in_file:
        for line in in_file:
            tup = make_tuple(line)
            shares.append(tup)

    secret = str(shamir.recover_secret(shares))
    flag = vigenere_cipher(cipher, secret)
    print(flag)
