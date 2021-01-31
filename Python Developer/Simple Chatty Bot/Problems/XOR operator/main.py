def xor(a, b):
    if bool(a) == bool(b):
        return False
    else:
        if a:
            return a
        else:
            return b
