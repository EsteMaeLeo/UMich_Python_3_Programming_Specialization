'''
open(filename,'r') Open a file called filename and use it for reading. This will return a reference to a file object.
open(filename,'w') Open a file called filename and use it for writing. This will also return a reference to a file object.
close filevariable.close() File use is complete.
'''
#all file at once
fileref = open("d:/code/data/data.txt", "r")
contents = fileref.read() # read all file
print(contents)
## other code here that refers to variable fileref
fileref.close()

#return a list of strings
fileref = open("d:/code/data/data.txt", "r")
lines = fileref.readlines() # read all file
print(lines[:4])
print("length", len(lines))
print("Printing using for")
for line in lines:
    print(line.strip())
## other code here that refers to variable fileref
fileref.close()

#rreturn list using fileref
fileref = open("d:/code/data/data.txt", "r")
print("Printing using for reference the object fileref",)
for line in fileref:
    print(line.strip())
## other code here that refers to variable fileref
fileref.close()

olympicsfile = open("d:/code/data/data.txt", "r")

for aline in olympicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()
