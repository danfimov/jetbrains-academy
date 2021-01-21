x = int(input())
y = int(input())

result = 8
if x in (1, 8):
    result -= 3
if y in (1, 8):
    result -= 3

if result == 2:
    print(result + 1)
else:
    print(result)