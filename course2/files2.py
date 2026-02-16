print("relative path")
fileref = open("../test/squares.txt", "w")
square = 0
for number in range(10):
   square = number * number
   print(str(square))
   fileref.write(str(square) + "\n")
fileref.close()

fileref = open("../test/squares.txt", "r")
print(fileref.read()[:10])

print("Open file using WITH")

fname = "../test/squares.txt"
with open(fname, 'r') as md:
    #print(lines.read())
    lines = md.readlines()
    for line in lines:
        print(line)

fname = "../test/squares2.txt"
with open(fname, 'w') as md:
    for number in range(10):
        square = number * number
        md.write(str(square) + "\n")

