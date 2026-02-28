
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

#Assign the first 30 characters of `assets/school_prompt.txt` as a string to the variable `beginning_chars`.

beginning_chars = None

# YOUR CODE HERE
#raise NotImplementedError()
beginning_chars = ""
fpath = "../test/school_prompt.txt"
with open(fpath, 'r') as f:
    beginning_chars = f.read()[:30]
    print(beginning_chars)

assert type(beginning_chars) == type(""), "beginning_chars is not a string"
assert len(beginning_chars) == 30, "beginning_chars is not assigned the correct length"
#**Challenge:** Using the file `assets/school_prompt.txt`, a
# assign the third word of every line to a list called `three`.

#three = None
three = []
fpath = "../test/school_prompt.txt"
with open(fpath, 'r') as file:
     for line in file:
          listline = line.split()
          three.append(listline[2])
print(three)          
# YOUR CODE HERE
#raise NotImplementedError()

three = []
fpath = "../test/school_prompt.txt"
with open(fpath, 'r') as file:
    for line in file:
        words = line.strip().split()
        if len(words) >= 3:
            three.append(words[2])

print(three)