def get_percentage(number, ndigits=None):
    number *= 100
    return str(round(number, ndigits)) + '%'
