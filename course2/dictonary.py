eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp)
value = eng2sp['two']
print(value)
print(eng2sp['one'])

#Del
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print("Dictionary: ", inventory)
del inventory['pears']
print("delete pears ", inventory)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory)
inventory['pears'] = 0
print("Assign value 0 to Pears", inventory)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory)
inventory['bananas'] = inventory['bananas'] + 200
print("Modify the value adding + 200 to banana", inventory)

numItems = len(inventory)
print("num elements: ",numItems)

mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers["Phelps"] = swimmers["Phelps"] + 5 
print(swimmers)

print("*****Methods******")
inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}
print("All inventory: ", inventory)
print("Oranges inventory: ", inventory["oranges"])

for key in inventory.keys():
    print(key, "has the value ", inventory[key])

keys = list(inventory.keys())
print("Transform a list of keys: ", keys)

#get values
#return tuples

for key in inventory.keys():
    print(key, "has the value ", inventory[key])