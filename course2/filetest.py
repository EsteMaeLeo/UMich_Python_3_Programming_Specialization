#Write code to print out the first 10 characters of “school_prompt2.txt”
fname = "../test/school_prompt2.txt"
with open(fname, 'r') as md:
    print(md.read()[:10])

#Write code to print the first character from each line of “school_prompt2.txt”    

fobject = "../test/school_prompt2.txt"
with open(fobject, 'r') as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line[0])

#Write code that, when executed, writes to a file “school_prompt3.txt” the numbers 0 to 19, 
# #each written on a separate line
fobject = "../test/school_prompt3.txt"
with open(fobject, 'w') as file:
    for number in range(20):
        file.write(f"{number}\n")
#Then write code and one or more `assert` statements that will test whether your code has worked correctly. 
# (Hint: read in the contents of the file and see if it’s what you thought should be written there.)

with open(fobject, 'r') as file:
    num = file.readlines()

expected = [f"{i}\n" for i in range(20)]

assert num == expected

#more robust
with open(fobject, 'r') as file:
    num = file.read()

# Split and clean each line
actual_numbers = [
    line.strip()                 # remove \n, \r\n, spaces
    for line in num.splitlines()
    if line.strip()              # skip empty lines
]

expected_numbers = [str(i) for i in range(20)]

assert actual_numbers == expected_numbers, \
    f"Expected {expected_numbers}\nGot     {actual_numbers}"


#Modern
filename = "school_prompt3.txt"

# Write
with open(filename, 'w') as f:
    f.writelines(f"{i}\n" for i in range(20))     # nice one-liner

# Test
with open(filename) as f:
    numbers = [line.strip() for line in f]

assert numbers == [str(i) for i in range(20)], "Wrong numbers in file"
print("All good!")

#The textfile, assets/travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the fileand save to the variable num
num = None
fpath = "../test/travel_plans.txt"
with open(fpath, "r") as travel:
        num = len(travel.read())
        print(num)
# YOUR CODE HERE
#raise NotImplementedError()

#We have provided a file called assets/emotion_words.txt that contains lines of words that \
# describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
num_words = 0
# YOUR CODE HERE
fpath = "../test/emotion_words.txt"
with open(fpath, "r") as f:
    lines = f.readlines()
    for line in lines:
        listline = line.split()
        num_words = num_words + len(listline)

print(num_words)
assert num_words == 48, "num_words is not assigned the correct value"


#Assign to the variable num_lines the number of lines in the file assets/school_prompt.txt.

num_lines = None
# YOUR CODE HERE
fpath = "../test/school_prompt.txt"
with open(fpath, 'r') as f:
   lines = f.readlines()
   num_lines = len(lines)
   print(num_lines) 
assert num_lines == 10, "num_lines is not assigned the correct value"  