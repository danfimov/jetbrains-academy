# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

d = {}
numbers = []
n = int(input())
for i in range(n):
    numbers.append(int(input()))
d = dict.fromkeys(groups)
i = 0
for number in numbers:
    d[groups[i]] = number
    i += 1
print(d)