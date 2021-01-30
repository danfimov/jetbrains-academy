n = int(input())

my_stack = [input() for i in range(n)]
print(*my_stack[::-1], sep='\n')
