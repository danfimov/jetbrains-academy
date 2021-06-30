# use the function blackbox(lst) that is already defined
lst = [1, 2, 3]


print('modifies' if id(blackbox(lst)) == id(lst) else 'new')