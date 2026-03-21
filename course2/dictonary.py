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

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print("sort keys")
inventory2 = inventory;

for akey in sorted((inventory2)):
    print("sorted: ", akey, "has the value ", inventory2[key])

print(list(inventory2.values()))

for k in inventory:
    print("Got key ", k)

for v in inventory.values():
    print("Got values", v)

print(list(inventory.items()))

for k, v in inventory.items():
    print("Got", k, "that maps to", v)    

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")


print("Inventory apples", inventory.get("apples"))
print("Inventory cherries", inventory.get("cherries"))

print("Inventory cherries", inventory.get("cherries",0))

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict.get("cat")//mydict.get("dog")
print(answer)

total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events)
print(events)