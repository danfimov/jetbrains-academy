n = int(input())
stack = []
for _i in range(n):
    user_input = input()
    if user_input == 'POP':
        stack.pop()
    else:
        command, number = user_input.split()
        number = int(number)
        stack.append(number)
while stack:
    print(stack.pop())