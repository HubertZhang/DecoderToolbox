from .util import PassValueDict


def skip2(s=""):
    print("Jump result")
    print(s[::2])
    print(s[1::2])
    return (s[::2], s[1::2])


def zigzag(s1="", s2=""):
    r1 = ""
    r2 = ""
    for i in range(len(s1)):
        if i % 2 == 0:
            r1 += s1[i]
            r2 += s2[i]
        else:
            r1 += s2[i]
            r2 += s1[i]
    return (r1, r2)


def divide_string(s="", skip=2):
    ret = []
    for i in range(0, len(s), skip):
        if i + skip > len(s):
            ret.append(s[i:])
        else:
            ret.append(s[i:i + skip])
    return ret


def divide_number_string(s="", skip=2, base=10):
    return [int(x, base) for x in divide_string(s, skip)]


def polybius(numbers=[]):
    polybius_square = ["abcde", "fghjk", "lmnop", "qrstu", "vwxyz"]
    return ''.join([polybius_square[int(x / 10) - 1][int(x % 10) - 1] for x in numbers])


def atbash_letter(s=""):
    r = ""
    for l in s:
        if 'a' <= l <= 'z':
            r += chr(ord('a') * 2 + 25 - ord(l))
        elif 'A' <= l <= 'Z':
            r += chr(ord('A') * 2 + 25 - ord(l))
        else:
            r += l
    return r


def atbash_number(s="", zero_to_zero=True):
    r = ""
    for l in s:
        if not zero_to_zero:
            if '0' <= l <= '9':
                r += chr(ord('0') * 2 + 9 - ord(l))
            else:
                r += l
        else:
            if '1' <= l <= '9':
                r += chr(ord('1') * 2 + 8 - ord(l))
            else:
                r += l

    return r


def atbash(s="", zero_to_zero=True):
    return atbash_letter(atbash_number(s, zero_to_zero=zero_to_zero))


def hex_atbash(s):
    r = ""
    for l in s:
        r += hex(15 - int(l, 16))[2:]
    return r


def lower_letter_to_number(s=""):
    return [ord(l) - ord('a') for l in s]


def binary_to_int(s="00000111"):
    return int(s, base=2)


def char_to_int_str(t):
    return "".join([str(char_to_int(x)) for x in t])


def char_to_int(t="0"):
    temp = ""
    for a in t:
        q = ord(a.lower())
        if ord('a') <= q <= ord('z'):
            temp += str(q - ord('a'))
        else:
            temp += a
    return int(temp)


def int_to_char(a=0):
    return chr(a + ord('a'))


def print_all_rot(s=""):
    for i in range(26):
        print(s)
        s = rot(s)


def symbol_to_int(s=''):
    t = "!@#$%^&*()"
    y = "1234567890"
    u = PassValueDict({t[i]: y[i] for i in range(10)})
    r = ""
    for x in s:
        if x in t:
            r += u[x]
        else:
            r += x
    return r


def rot(s="", i=1):
    r = ""
    for l in s:
        if 'a' <= l <= 'z':
            r += chr(ord('a') + (ord(l) - ord('a') + i) % 26)
        elif 'A' <= l <= 'Z':
            r += chr(ord('A') + (ord(l) - ord('A') + i) % 26)
        elif '0' <= l <= '9':
            r += chr(ord('0') + (ord(l) - ord('0') + i) % 10)
        else:
            r += l
    return r


def rot_by_char(s="", i="a", reverse=False):
    i = i.lower()
    if '0' <= i <= '9':
        i = int(i)
    elif 'a' <= i <= 'm':
        i = ord(i) - ord('a')
    else:
        i = ord(i) - ord('a') - 26
    if reverse:
        i = -i
    return rot(s, i)


def mirror(s=""):
    ori = "1234567890qwertyuiopasdfghjkl;zxcvbnm,./!@#$%^&*()QWERTYUIOPASDFGHJKL:ZXCVBNM<>?"
    new = "0987654321poiuytrewq;lkjhgfdsa/.,mnbvcxz)(*&^%$#@!POIUYTREWQ:LKJHGFDSA?><MNBVCXZ"
    cov = PassValueDict({ori[i]: new[i] for i in range(len(ori))})
    return ''.join([cov[x] for x in s])


def vmirror(s=""):
    ori = "1234567890qwertyuiopasdfghjkl;zxcvbnm,./!@#$%^&*()QWERTYUIOPASDFGHJKL:ZXCVBNM<>?"
    new = "zxcvbnm,./asdfghjkl;qwertyuiop1234567890ZXCVBNM<>?ASDFGHJKL:QWERTYUIOP!@#$%^&*()"
    cov = PassValueDict({ori[i]: new[i] for i in range(len(ori))})
    return ''.join([cov[x] for x in s])


def int_to_roman(input):
    """
    Convert an integer to Roman numerals.

    Examples:
    >>> int_to_roman(0)
    Traceback (most recent call last):
    ValueError: Argument must be between 1 and 3999

    >>> int_to_roman(-1)
    Traceback (most recent call last):
    ValueError: Argument must be between 1 and 3999

    >>> int_to_roman(1.5)
    Traceback (most recent call last):
    TypeError: expected integer, got <type 'float'>

    >>> for i in range(1, 21): print int_to_roman(i)
    ...
    I
    II
    III
    IV
    V
    VI
    VII
    VIII
    IX
    X
    XI
    XII
    XIII
    XIV
    XV
    XVI
    XVII
    XVIII
    XIX
    XX
    >>> print int_to_roman(2000)
    MM
    >>> print int_to_roman(1999)
    MCMXCIX
    """
    if type(input) != type(1):
        raise TypeError("expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = ""
    for i in range(len(ints)):
        count = int(input / ints[i])
        result += nums[i] * count
        input -= ints[i] * count
    return result


def roman_to_int(input):
    """
    Convert a roman numeral to an integer.

    >>> r = range(1, 4000)
    >>> nums = [int_to_roman(i) for i in r]
    >>> ints = [roman_to_int(n) for n in nums]
    >>> print r == ints
    1

    >>> roman_to_int('VVVIV')
    Traceback (most recent call last):
     ...
    ValueError: input is not a valid roman numeral: VVVIV
    >>> roman_to_int(1)
    Traceback (most recent call last):
     ...
    TypeError: expected string, got <type 'int'>
    >>> roman_to_int('a')
    Traceback (most recent call last):
     ...
    ValueError: input is not a valid roman numeral: A
    >>> roman_to_int('IL')
    Traceback (most recent call last):
     ...
    ValueError: input is not a valid roman numeral: IL
    """
    if type(input) != type(""):
        raise TypeError("expected string, got %s" % type(input))
    input = input.upper()
    nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    ints = [1000, 500, 100, 50, 10, 5, 1]
    places = []
    for c in input:
        if not c in nums:
            raise ValueError("input is not a valid roman numeral: %s" % input)
    for i in range(len(input)):
        c = input[i]
        value = ints[nums.index(c)]
        # If the next place holds a larger number, this value is negative.
        try:
            nextvalue = ints[nums.index(input[i + 1])]
            if nextvalue > value:
                value *= -1
        except IndexError:
            # there is no next place.
            pass
        places.append(value)
    sum = 0
    for n in places: sum += n
    # Easiest test for validity...
    if int_to_roman(sum) == input:
        return sum
    else:
        raise ValueError('input is not a valid roman numeral: %s' % input)
