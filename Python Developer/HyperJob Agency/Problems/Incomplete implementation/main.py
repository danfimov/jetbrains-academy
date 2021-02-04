def startswith_capital_counter(names):
    result = 0
    for name in names:
        if name[0].isupper():
            result += 1
    return result