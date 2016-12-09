import re

morseAlphabet = {
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

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())
validMorse = set([x for x in morseAlphabet.keys() if
                  x.replace(".", "=").replace("-", ".").replace("=", "-") in inverseMorseAlphabet.keys()])


# parse a morse code string positionInString is the starting point for decoding
def decodeMorse(code=""):
    return ''.join([inverseMorseAlphabet[x] for x in re.split("[\\\s]", code)])


# encode a message in morse code, spaces between words are represented by '/'
def encodeToMorse(message="", sep = " "):
    return sep.join([morseAlphabet[x.upper()] for x in message])


def flipByMorse(message=""):
    return decodeMorse(flipByMorse(encodeToMorse(message)))


def canBeReverse(message=""):
    for x in message:
        if x not in validMorse:
            return False
    return True


def flipMorse(message=""):
    return message.replace(".", "=").replace("-", ".").replace("=", "-")