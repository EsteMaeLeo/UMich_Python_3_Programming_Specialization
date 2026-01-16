x = True
y = False
print(x or y)
print(x and y)
print(not x)

x = 5
print(x > 0 and x < 10)

n = 25
print(n % 2 == 0 or n % 3 == 0)

total_weight = int(input('Enter total weight of luggage:'))
num_pieces = int(input('Number of pieces of luggage?'))

if num_pieces != 0 and total_weight / num_pieces > 50:
   print('Average weight is greater than 50 pounds -> $100 surcharge.')

print('Luggage check complete.')

print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')

print('a' in 'a')
print('apple' in 'apple')
print('' in 'a')
print('' in 'apple') #that a string is a substring of itself, and the empty string is a substring of any other string.

print('x' not in 'apple')
print("a" in ["a", "b", "c", "d"])
print(9 in [3, 2, 9, 10, 9.0])
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])

print("a" in ["apple", "absolutely", "application", "nope"]) #python is checking whether or not an element of the list is the string “a” - nothing more or less than that.

assert type(9//5) == int
#assert type(9.0//5) == int #error because fail the ttest

lst = ['a', 'b', 'c']

first_type = type(lst[0])
for item in lst:
    assert type(item) == first_type

lst2 = ['a', 'b', 'c', 17]
first_type = type(lst2[0])
#for item in lst2:
    #assert type(item) == first_type
lst = ['a', 'b', 'c']

assert len(lst) < 10

x = 15

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")

x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")

#Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, 
#add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. 
#Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly.
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
reps = []
for percent in percent_rain:
    if percent > 90:
        reps.append("Bring an umbrella.")
    elif percent > 80:
        reps.append("Good for the flowers?")
    elif percent > 50:
        reps.append("Watch out for clouds!")
    else:
        reps.append("Nice day!")
print(reps)

x = 66
output = []

if x > 63:
    output.append(True)
elif x > 55:
    output.append(False)
else:
    output.append("Neither")

if x > 67:
    output.append(True)
else:
    output.append(None)
