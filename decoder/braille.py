brailleChars = {
    'a': '1',
    'b': '12',
    'c': '14',
    'd': '145',
    'e': '15',
    'f': '124',
    'g': '1245',
    'h': '125',
    'i': '24',
    'j': '245',
    'k': '13',
    'l': '123',
    'm': '134',
    'n': '1345',
    'o': '135',
    'p': '1234',
    'q': '12345',
    'r': '1235',
    's': '234',
    't': '2345',
    'u': '136',
    'v': '1236',
    'w': '2456',
    'x': '1346',
    'y': '13456',
    'z': '1356',
    '1': '2',
    '2': '23',
    '3': '25',
    '4': '256',
    '5': '26',
    '6': '235',
    '7': '2356',
    '8': '236',
    '9': '35',
    '0': '356',
}

reversedBrailleChar = dict((v, k) for (k, v) in brailleChars.items())


def decodeBrailleChar(bits=""):
    t = ""
    for i in range(6):
        if bits[i] == ".":
            t += str(i + 1)
    return reversedBrailleChar[t]


def readBrailleMorse(message=""):
    lines = [message[i::3] for i in range(3)]
    for l in lines:
        tmp = ""
        for i in range(len(l)):
            tmp += l[i]
            if i % 2 == 1:
                tmp += "|"
        print(tmp)
    r = ""
    for i in range(len(lines[0])):
        for j in range(3):
            r += lines[j][i]
    return ''.join([decodeBrailleChar(r[a:a + 6]) for a in range(0, len(r), 6)])
