from typing import List

from .util import PassValueDict


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


def dvorak(s=""):
    ori = "',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz"
    new = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
    cov = PassValueDict({ori[i]: new[i] for i in range(len(ori))})
    return ''.join([cov[x] for x in s])


phone_pad = [
    "", "abc", "def",
    "ghi", "jkl", "mno",
    "pqrs", "tuv", "wxyz"
]


def phone_to_str(input: List[str]):
    return "".join(phone_pad[int(x[0]) - 1][len(x) - 1] for x in input)


keyboard_pad = [
    "p", "qaz", "wsx", "edc",
    "rfv", "tgb", "yhn",
    "ujm", "ik", "ol",
]


def keyboard_to_str(input: List[str]):
    return "".join([keyboard_pad[int(x[0])][len(x) - 1] for x in input])
