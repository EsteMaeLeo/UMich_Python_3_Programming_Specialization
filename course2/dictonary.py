eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp)
value = eng2sp['two']
print(value)
print(eng2sp['one'])

#Del
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print("Dictionary: ", inventory)
del inventory['pears']
print("delete ", inventory)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory)
inventory['pears'] = 0
print(inventory)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory)
inventory['bananas'] = inventory['bananas'] + 200
print(inventory)

numItems = len(inventory)
print(numItems)