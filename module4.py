
#lists are mutable. This means we can change an item in a list by accessing it directly as part of the assignment statement.
fruit = ["banana", "apple", "cherry"]
print(fruit)

print("Modify")
fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
print(alist)
alist[1:3] = ['x', 'y']
print(alist)

print("Delete")
alist = ['a', 'b', 'c', 'd', 'e', 'f']
print(alist)
alist[1:3] = []
print(alist)

print("Insert")
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

#Strings are immutable, which means you cannot change an existing string. The best you can do is create a new string that is a variation on the original.
#tuples are like immutable lists.
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was

phrase1 = "many moons"
print(phrase1)
phrase_expanded = phrase1 + " and many stars"
print(phrase_expanded)
phrase_larger = phrase_expanded + " litter"
print(phrase_larger)
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
print(phrase_complete)
excited_phrase_complete = phrase_complete[:-1] + "!"
print(excited_phrase_complete)

#Delete list
print("delete in the list")
a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)


print("****************************************")
#Objects and References
a = "banana"
b = "banana"
#two names refer to the same object using the is operator. 
print(a is b)
#. Python assigns every object a unique id and when we ask a is b what python is really doing is checking to see if id(a) == id(b).
#he answer is True. This tells us that both a and b refer to the same object, and that it is the second of the two reference diagrams
#that describes the relationship. Python assigns every object a unique id and when we ask a is b what python is really doing is checking to see if id(a) == id(b
a = "banana"
b = "banana"

print(id(a))
print(id(b))
print(a==b)

a = [81,82,83]
b = [81,82,83]

print(a is b)

print(a == b)

print(id(a))
print(id(b))

#Aliasing
a = [81, 82, 83]
b = a
print(a is b)
print("*")
a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

#Cloning Lists
print("Cloning Lists")
a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)

alist = [4,2,8,6,5]
blist = alist * 2
blist[3] = 999
print(blist)
print(alist)

# Mutating Methods
print(" Mutating Methods")
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)