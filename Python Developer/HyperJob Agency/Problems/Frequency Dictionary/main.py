s = list(input().split())

d = {}
for elem in s:
    elem = elem.lower()
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

for key, value in d.items():
    print(key, value)