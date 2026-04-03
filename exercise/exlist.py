#basic creation
fruits = ["apple", "banana", "cherry"]
print(fruits)
numbers = [1, 2, 3, 4, 5]
print(numbers)
mixed = [1, "hello", 3.14, True, None]
print(mixed)

fruits.append("melon")
print("adding melon" ,fruits)
fruits.extend(["fig", "kiwi", "grape"])
print("Extend adding multiples: ", fruits)

fruits.insert(1, "avocado") 
print("insert position 1: ", fruits)
fruits.remove("banana")
print("remove banana", fruits)
popItem = fruits.pop()
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
print(nums[0:3])
print(nums[3:5])
#Use the syntax list[start:stop:step]. By leaving start and stop empty and setting 
# step to 2, you tell Python to start at the beginning, go to the end, and skip every other item.
#First Colon (:): Represents the start and stop values. When left empty, Python 
# defaults to the very beginning and the very end of the list.
#Second Colon (:): Separates the range from the step value.
#Step (2): Specifies the interval. A step of 2 selects the element at 
# index 0, then 2, then 4, and so on
print(nums[::2])

listNames = []
for i in range(3):
    name = input(f"Enter name {i+1}: ")
    listNames.append(name)
#listNames.extend([name1, name2, name3])
print(listNames)
for i in range(len(listNames) -1, -1, -1):
    print(listNames[i])