#Write code to print out the first 10 characters of “school_prompt2.txt”
fname = "../test/school_prompt2.txt"
with open(fname, 'r') as md:
    print(md.read()[:10])

#Write code to print the first character from each line of “school_prompt2.txt”    

fobject = "../test/school_prompt2.txt"
with open(fobject, 'r') as md:
    lines = md.readlines()
    print(lines)
    for line in lines:
        print(line[0])

#The textfile, assets/travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the fileand save to the variable num
num = None
fpath = "../test/travel_plans.txt"
with open(fpath, "r") as travel:
        num = len(travel.read())
        print(num)
# YOUR CODE HERE
#raise NotImplementedError()