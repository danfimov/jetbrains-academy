def final_deposit_amount(*interest, amount=1000):
    result = amount
    for elem in interest:
        result = result * (1 + elem / 100)
    return round(result, 2)