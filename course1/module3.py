x = True
y = False
print(x or y)
print(x and y)
print(not x)

x = 5
print(x > 0 and x < 10)

n = 25
print(n % 2 == 0 or n % 3 == 0)

#total_weight = int(input('Enter total weight of luggage:'))
#num_pieces = int(input('Number of pieces of luggage?'))

#if num_pieces != 0 and total_weight / num_pieces > 50:
#   print('Average weight is greater than 50 pounds -> $100 surcharge.')

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

x = 3
y = 4
if x < y:
    z = x
else:
    if x > y:
        z = y
    else:
        ## x must be equal to y
        assert x==y
        z = 0

phrase = "What a wonderful day to program"
tot = 0
for char in phrase:
    if char != " ":
        tot = tot + 1
print(tot)

s = "what if we went to the zoo"
x = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print(x)

nums = [9, 3, 8, 11, 5, 29, 2]
best_num = 0
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

nums = [9, 3, 8, 11, 5, 29, 2]
best_num = nums[0]
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)


words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for word in words:
    if len(word) > 3:
        num_words += 1
print(num_words)
#Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. 
#Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words:
    if word[len(word)-1] == "e":
        past_tense.append(word+"d")
    else:
        past_tense.append(word+"ed")
print(past_tense)


#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with 
#every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store 
#the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0. Hard-coded answers will receive no credit.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = 0
rainfall_mi = rainfall_mi.split(',')
for rain_month in rainfall_mi:
    if float(rain_month) > 3.0:
        num_rainy_months +=1

print(num_rainy_months)

#The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including 
#one-letter words. Store the result in the variable same_letter_count.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
sentence = sentence.split(' ')
for word in sentence:
    if len(word) == 1:
        same_letter_count += 1
        print(word)
    elif word[0] ==  word[len(word)-1]:
        same_letter_count += 1
        print(word)
print(same_letter_count)

#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
#HINT 1: Use the accumulation pattern!
#HINT 2: the in operator checks whether a substring is present in a string.
#Hard-coded answers will receive no credit.

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for item in items:
    if "w" in item:
        acc_num += 1
print(acc_num)

#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
#Note 1: be sure to not double-count words that contain both an a and an e.
#HINT 1: Use the in operator.
#HINT 2: You can either use or or elif.
#Hard-coded answers will receive no credit

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
sentence = sentence.split(" ")
for word in sentence:
    if "a" in word: 
        num_a_or_e +=1
    elif "e" in word:
        num_a_or_e +=1
print(num_a_or_e)

#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem,
#vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
num_vowels = 0
vowels = ['a','e','i','o','u']
for word in s:
    if word in vowels:
        num_vowels +=1

print(num_vowels)