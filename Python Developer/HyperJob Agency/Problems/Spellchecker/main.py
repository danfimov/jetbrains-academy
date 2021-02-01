dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

flag = True

user_input = list(input().split())
for word in user_input:
    if word in dictionary:
        pass
    else:
        print(word)
        flag = False

if flag:
    print('OK')
