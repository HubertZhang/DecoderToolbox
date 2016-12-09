from decoder.basic import *


def encode_vigenere(cipher="", key=""):
    return ''.join([rot(cipher[i], ord(key[i % len(key)]) - ord('a')) for i in range(len(cipher))])


def decode_vigenere(cipher="", key=""):
    return ''.join([rot(cipher[i], ord('a') - ord(key[i % len(key)])) for i in range(len(cipher))])


def encode_autokey(cipher="", key=""):
    key1 = key + cipher
    return ''.join([rot(cipher[i], ord(key1[i % len(key1)]) - ord('a')) for i in range(len(cipher))])


def decode_autokey(cipher="", key=""):
    ori = ""
    for i in range(len(cipher)):
        if i < len(key):
            ori += rot(cipher[i], ord('a') - ord(key[i]))
        else:
            ori += rot(cipher[i], ord('a') - ord(ori[i - len(key)]))
    return ori
