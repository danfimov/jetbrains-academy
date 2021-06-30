s = input()
stack = []
for elem in s:
    if elem == '(':
        stack.append(elem)
    elif elem == ')' and stack:
        stack.pop()
    elif elem == ')' and len(stack) == 0:
        stack.append(')')
        break

if stack:
    print('ERROR')
else:
    print('OK')
