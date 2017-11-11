from decoder.basic import *


def encode_vigenere(cipher="", key=""):
    return ''.join([rot_by_char(s, key[i % len(key)]) for i, s in enumerate(cipher)])


def decode_vigenere(cipher="", key=""):
    return ''.join([rot_by_char(s, key[i % len(key)], reverse=True) for i, s in enumerate(cipher)])


def encode_autokey(cipher="", key=""):
    key1 = key + cipher
    return ''.join([rot_by_char(s, key1[i % len(key1)]) for i, s in enumerate(cipher)])


def decode_autokey(cipher="", key=""):
    ori = ""
    for i, s in enumerate(cipher):
        if i < len(key):
            ori += rot_by_char(s, key[i], reverse=True)
        else:
            ori += rot_by_char(s, ori[i - len(key)], reverse=True)
    return ori
