# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
print('min:', min(test_dict, key=lambda elem: test_dict[elem]))
print('max:', max(test_dict, key=lambda elem: test_dict[elem]))