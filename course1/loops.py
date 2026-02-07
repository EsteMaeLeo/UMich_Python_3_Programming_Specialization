name = ['Charlie', 'Joe', 'Katty']

for aname in name:
    print(aname, aname.count('e')) #count how many e on the name

for char in 'AC101':
    print(char)

for index in range(5):
    square = index * index
    print('The square of ',index, 'is', square)

for achar in "Go Spot Go":
    print(achar)

for achar in "Go Spot Go":
    print(type(achar))
nums = [1,2,3,4,5,6,7,8,9,10]
nums2 = range(1,11)

print(nums, nums2)

acum = 0
for w in nums:
    acum = acum + w

print(acum)
acum = 0
for w in nums2:
    acum = acum + w

print(acum)

print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
count = 0
for char in str1:
    count = count + 1
print(count)

numbers = list(range(0,41))
print(numbers)
sum1 = 0
for number in numbers:
    sum1 = sum1 + number
print(sum1)

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

w = range(1, 11)

tot = 0
print("***** Before the For Loop ******")
for num in w:
    print("***** A New Loop Iteration ******")
    print("Value of num:", num)
    tot += num
    print("Value of tot:", tot)
print("***** End of For Loop *****")
print("Final total:", tot)

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for element in str_list:
    print(len(element))

print('********************')
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0

for char in original_str:
    num_chars = num_chars + 1
print(num_chars)    

print('********************')
addition_str = "2+5+10+20"
sum_val = 0
addition_str = addition_str.split('+')
for number in addition_str:
    sum_val = sum_val + int(number)
print(sum_val)    

print('********************')
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
avg_temp = 0
week_temps_f  = week_temps_f.split(',')
for temperature in week_temps_f:
    avg_temp = avg_temp + float(temperature) 
avg_temp = avg_temp / len(week_temps_f) 
print(avg_temp)

#Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.
print('********************')
nums = list(range(0,68))
print(nums)

print('********************')
#Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).
original_str = "The quick brown rhino jumped over the extremely lazy fox"
original_str = original_str.split(" ")
print(original_str )
num_words_list = []
for char in original_str:
    num_words_list = num_words_list + [len(char)]
print(num_words_list)

num_words_list = []
original_str = "The quick brown rhino jumped over the extremely lazy fox"
for word in original_str.split():
    num_words_list.append(len(word))
print(num_words_list)
print('********************')
#Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").
lett = ""
lett = "b" * 7
print(lett)

print('********************')
#Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, 
#but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get 
#tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)