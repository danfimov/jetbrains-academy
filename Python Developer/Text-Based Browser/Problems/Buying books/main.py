n = int(input())
stack = []
read = []
for _i in range(n):
    user_input = input()
    if user_input == 'READ':
        read.append(stack.pop())
    else:
        command, book = user_input.split(maxsplit=1)
        stack.append(book)
print(*read, sep='\n')
