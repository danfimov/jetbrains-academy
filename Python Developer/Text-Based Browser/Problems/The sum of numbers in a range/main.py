def range_sum(numbers, start, end):
    return sum(elem for elem in numbers if start <= elem <= end)


input_numbers = list(map(int, input().split()))
a, b = map(int, input().split())
print(range_sum(input_numbers, a, b))
