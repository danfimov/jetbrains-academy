def sq_sum(*args):
    result = 0
    for elem in args:
        result += elem ** 2
    return float(result)
