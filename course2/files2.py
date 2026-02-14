print("relative path")
fileref = open("../../../data/squares2.txt", "w")
square = 0
for number in range(10):
   square = number * number
   print(str(square))
   fileref.write(str(square) + "\n")
fileref.close()

fileref = open("../../../data/squares.txt", "r")
print(fileref.read()[:10])