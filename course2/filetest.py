#Write code to print out the first 10 characters of “school_prompt2.txt”
fname = "../test/school_prompt2.txt"
with open(fname, 'r') as md:
    print(md.read()[:10])
    