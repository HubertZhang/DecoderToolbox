import re

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
    "0": "-----"
}

inverse_morse_alphabet = dict((v, k) for (k, v) in morse_alphabet.items())
valid_morse_alphabet = set([x for x in morse_alphabet.keys() if
                            x.replace(".", "=").replace("-", ".").replace("=", "-") in inverse_morse_alphabet.keys()])


# parse a morse code string positionInString is the starting point for decoding
def decode_morse(code=""):
    return ''.join([inverse_morse_alphabet[x] for x in re.split("[\\\s]", code)])


# encode a message in morse code, spaces between words are represented by '/'
def encode_morse(message="", sep=" "):
    return sep.join([morse_alphabet[x.upper()] for x in message])


def decode_by_flip_morse(message=""):
    return decode_morse(decode_by_flip_morse(encode_morse(message)))


def flip_morse_validation(message=""):
    for x in message:
        if x not in valid_morse_alphabet:
            return False
    return True


def flip_morse_string(message=""):
    return message.replace(".", "=").replace("-", ".").replace("=", "-")
