for i in range(1,11):
    with open('file'+str(i) + '.txt', 'w') as file:
        print(i, file=file)