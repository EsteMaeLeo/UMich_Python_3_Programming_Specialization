nums = [3,5,8]
accum =[]
for num in nums:
    square = num**2
    accum.append(square)
print(accum)

alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)

lst= [3,0,9,4,1,7]
new_list=[]
for i in range(len(lst)):
   new_list.append(lst[i]+5)
print(new_list)

print("For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.")
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for verb in verbs:
    ing.append(verb+"ing")
print(ing)

print("Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.")
numbs = [5, 10, 15, 20, 25]
newlist = []
for numb in numbs:
    newlist.append(numb+5)
print(newlist)

print("Given the list of numbers, numbs, modifiy the list numbs so that each of the original numbers are increased by 5. Note this is not an accumulator pattern problem, but its a good review")
numbs = [5, 10, 15, 20, 25]
for i in range(len(numbs)):
    print(i)
    numbs[i] = numbs[i]+5
print(numbs)

print("For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.")
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums = []
for num in lst_nums:
    larger_nums.append(num*2)
print(larger_nums)

print("ACCUMULATOR STRING")
s = "dog"
ac = ""
for c in s:
    ac = ac + c + "-"
    s = s + c + "-"
print(ac)
print(s)

s = "Murphy"
ac = ""
for c in s:
    ac = c + ac

print(ac)

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for s in str1:
    chars.append(s)
print(chars)

s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)

output = ""
for i in range(35):
    output = output + "a"
print(output)

print("Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars.")

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for char in str1:
    chars.append(char)
print(chars)

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

for color in colors:
    print(color)

colors = ["Red", "Orange", "Indigo"]
#prevent infinite loop	
for color in colors:    
    if color[0] in ["A", "E", "I", "O", "U"]:
        colors.append(color)
	
    print(colors)
	
    if len(colors)>6:
        break

x = ["dogs", "cats", "birds", "reptiles"]
y = x
print(id(y))
print(id(x))
x += ['fish', 'horses']
print(id(y))
print(id(x))
print(x)
print(y)
y = y + ['sheep']
# the behavior of obj = obj + object_two is different than obj += object_two when obj is a list. The first 
#version makes a new object entirely and reassigns to obj. The second version changes the original object so that 
#the contents of object_two are added to the end of the first.
print(id(y))
print(id(x))
print(x)
print(y)

a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(id(a))
print(id(quiet))
print(a)
print(quiet)

lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1
print(s)

print("For each character in the string saved in ael, append that character to a list that should be saved in a variable app.")
ael = "python!"
app = []
for char in ael:
    app.append(char)
print(app)

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for wrd in wrds:
    past_wrds.append(wrd + "ed")
print(past_wrds)