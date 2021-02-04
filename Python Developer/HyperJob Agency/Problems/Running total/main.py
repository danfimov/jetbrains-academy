s = input()
a = [int(elem) for elem in s]
b = []
for i in range(len(a)):
    sum_elem = 0
    for j in range(i+1):
        sum_elem += a[j]
    b.append(sum_elem)
print(b)