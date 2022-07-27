import re
from random import choice
from string import ascii_uppercase, digits

symbols = ascii_uppercase + digits


def is_ascii(s: str) -> bool:
    return re.match('^[\x00-\x7F]+$', s) is not None


def generate_key() -> str:
    return '-'.join([''.join(choice(symbols) for i in range(5)) for _ in range(4)])


def validate_key(key: str) -> bool:
    segments = key.split('-')
    segments_is_ascii = list(map(is_ascii, segments))
    return all([len(segments) == 4, segments_is_ascii[0], len(set(segments_is_ascii)) == 1])
