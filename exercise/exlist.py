#basic creation
fruits = ["apple", "banana", "cherry"]
print(fruits)
numbers = [1, 2, 3, 4, 5]
print(numbers)
mixed = [1, "hello", 3.14, True, None]
print(mixed)

fruits.append("melon") # adds one item at the end
print("adding melon" ,fruits) 
fruits.extend(["fig", "kiwi", "grape"]) # adds multiple items
print("Extend adding multiples: ", fruits)

fruits.insert(1, "avocado")  # insert at specific position
print("insert position 1: ", fruits)
fruits.remove("banana") # remove first occurrence
print("remove banana", fruits)
popItem = fruits.pop() # remove and return last item (or index)
print("Last Item: ", popItem)
print("cherry index", fruits.index("cherry"))
fruits.append("apple")
print("Count apples: ", fruits.count("apple"))

"""
Exercises (do all 3)

Create a list called shopping with 5 items.
Add one more item with append, insert an item at position 2, remove the 3rd item, 
then print the final list and its length.
Given nums = [10, 20, 30, 40, 50], use slicing to get:
The first 3 numbers
The last 2 numbers
Every second number (10, 30, 50)

Write a small program that asks the user for 3 names, stores them in a list, then prints them in reverse order without using reverse() or [::-1] yet (you can use a loop or negative indexing creatively).
"""
shopping =["Intel CPU", "DDR5", "SSD", "keyboard", "mouse"]
shopping.append("headphones")
shopping.insert(2, "Monitor")
shopping.remove("SSD")
print("list: ", shopping, "Lenght", len(shopping))

nums = [10, 20, 30, 40, 50]
print("First 3 numbers:", nums[0:3])
print("Last 2 numbers:", nums[3:5])        # or nums[-2:] is cleaner
print("Last 2 numbers:",  nums[-2:]) 
#Use the syntax list[start:stop:step]. By leaving start and stop empty and setting 
# step to 2, you tell Python to start at the beginning, go to the end, and skip every other item.
#First Colon (:): Represents the start and stop values. When left empty, Python 
# defaults to the very beginning and the very end of the list.
#Second Colon (:): Separates the range from the step value.
#Step (2): Specifies the interval. A step of 2 selects the element at 
# index 0, then 2, then 4, and so on
#range(start, stop, step)
print("Every second number:", nums[::2])

listNames = []
#for i in range(3):
#    name = input(f"Enter name {i+1}: ")
#    listNames.append(name)
#listNames.extend([name1, name2, name3])
print(listNames)
#range(start, stop, step)
for i in range(len(listNames) -1, -1, -1):
    print(listNames[i])


mena = ["John","Eric","Charlie","Lucas", "Kate"]
print(listNames[len(listNames)-1:])

# Classic way
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# Pythonic way (one line!)
squares = [x**2 for x in range(12)]    
print(squares)

# With condition
even_squares = [x**2 for x in range(12) if x % 2 ==0]
print(even_squares)

# copying
a = [1,2,3]
b = a # b is just another name for the same list
print("list a: ", a, " List b: ", b)
b.append(4) # → [1, 2, 3, 4]  ← both changed!
print("list a: ", a, " List b: ", b)

c = a.copy() # shallow copy (list method)
print("List c: ", c)
d = a[:] # slicing copy
print("List d: ", d)
import copy
e = copy.deepcopy(a) # only needed for nested lists
print("List e: ", e)

#Sorting & Advanced Methods
numbers = [x for x in range(21)]
numbers=[22,11,55,0,1]
print(numbers)
numbers.sort() # in-place, ascending
print(numbers)
numbers.sort(reverse=True)        # descending
print(numbers)

words = ['banana', "apple", "cherry", "melon"]
print(words)
words.sort(key=len) # sort by length
print(words)

# sorted() function returns a NEW list
new_list = sorted(words, key=len, reverse=True)
print(new_list)

#Use a list comprehension to create a list of all even numbers from 0 to 50.
#numbers = [x for x in range(51) if x % 2 == 0]
numbers = list(range(0, 51, 2))
print(numbers)

#Given names = ["Alice", "bob", "Charlie", "dave"], create a new list where every name is capitalized using a list capitalized using a list comprehension.
names = ["Alice", "bob", "Charlie", "dave"]
newNames = [name.capitalize() for name in names]
print(newNames)

#You have this list of tuples:
#students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
#Sort it by score (descending) using sorted() with a key function.
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
newStudents = sorted(students, key=lambda student: student[1], reverse=True)
print(newStudents)

##LEVEL 3###
### RECAP
# Dangerous - both variables point to the same list
a = [1, 2, 3]
b = a          # This is NOT a copy!
b.append(99)
print(a)       # [1, 2, 3, 99]  ← a also changed!
print(b)

# Correct ways to make a shallow copy
c = a.copy()          # Recommended
print(c)
c.append(1)
print("original: ", a, "c = a.copy()", c)
d = a[:]              # Slicing (very common)
print("Slicing d: ", d)
e = list(a)           # Also fine
print("e = list(a) : ", e)

# Deep copy - needed when you have nested lists
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
print("nested " ,nested,"copy.deepcopy(nested) ", deep )

nested[0][0] = 999
print(deep)           # Still [[1, 2], [3, 4]]
print(nested)
deep2 = [[x,x] for x in range(20) if x % 2 == 0 ]
print(deep2)

# Shallow copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original)
print(shallow)

# Matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[1][2]) # → 6  (row 1, column 2)

for row in matrix:
    print(row)
compMatrix = [[2] * 4 for _ in range(3)]# 3 rows × 4 columns
print(compMatrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix, len(matrix[0]))

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transposed)
# Result: [[1, 4], [2, 5], [3, 6]]

from collections import deque

# Create a queue
q = deque(["task1", "task2", "task3"])

q.append("task4")           # Add to the right (enqueue)
print(q)
print(q.popleft())          # Remove from the left (dequeue) → task1

# Also supports appendleft() and pop() for stack behavior

print_queue = deque()
print(print_queue)
print_queue.append("document.pdf")
print_queue.append("cv.pdf")
print_queue.append("photo.jpg")
print("Jobs in queue ", list(print_queue))

while print_queue:
    current = print_queue.popleft()
    print(f"Printing: {current}")
    
#Level 3 Exercises

#Flatten this nested list into a single list using only a list comprehension: 
nested = [[1,2,3], [4,5], [6,7,8,9]]
newList = [element[i] for element in nested for i in range(len(element))]
print(newList)

#Implement a function that takes a list of numbers and returns a new list with only the numbers that are greater than the average of the list (use list comprehension + sum/len).
def list_average(list):
    averageList = [avg for number in list avg = avg + number ]
    return averageList

average_list =list_average(newList)
print(average_list)

#Create a queue using deque and simulate a simple print queue: add 5 jobs, then process (remove) them one by one.