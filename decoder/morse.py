import re

from .util import default_dict_factory

morse_alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

inverse_morse_alphabet = default_dict_factory({v: k for (k, v) in morse_alphabet.items()}, default='*')


# parse a morse code string positionInString is the starting point for decoding
def decode_morse(code=""):
    ret = ''
    for x in re.split("[/\\s]", code):
        try:
            ret += inverse_morse_alphabet[x]
        except KeyError:
            ret += "*"
    return ret


# encode a message in morse code, spaces between words are represented by '/'
def encode_morse(message="", sep=" "):
    return sep.join([morse_alphabet[x.upper()] for x in message])


def decode_by_flip_morse(message=""):
    return decode_morse(flip_morse_string(encode_morse(message)))


def flip_morse_string(message=""):
    return message.replace(".", "=").replace("-", ".").replace("=", "-")


def convert_morse_to_binary(message=""):
    return message.replace(".", "1").replace("-", "0")
