
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
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was
