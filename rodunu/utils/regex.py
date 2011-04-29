import re

def is_fraction(val):
    regex = re.compile('(\d+)(\s)?(\d+)?(/\d+)?', re.IGNORECASE)
    m = regex.search(val)
    if m:
        return True
    else:
        return False


def is_float(val):
    regex = re.compile('([+-]?\d*\.\d+)(?![-+0-9\.])', re.IGNORECASE)
    m = regex.search(val)
    if m:
        return True
    else:
        return False