# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

big_new_family = {}
big_new_family.update(first_family)
big_new_family.update(second_family)

print(big_new_family)