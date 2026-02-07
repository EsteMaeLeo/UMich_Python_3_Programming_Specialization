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

olympicsfile = open("d:/code/data/athlete_events.csv", "r")
contents = olympicsfile.read()
print(len(contents))
#for aline in olympicsfile.readlines():
#    values = aline.split(" ")
#    print(values)
    #if values[14] == "NA" and  values[9] == 2000: 
    #    print(values[1], "is from", values[6], "and is on the roster for", values[12])

olympicsfile.close()

olympicsfile = open("d:/code/data/athlete_events.csv", "r")
#lines = 0
contents = olympicsfile.readlines()
print(len(contents))

olympicsfile.close()

#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
fileref = open("d:/code/data/emotion_words2.txt", "r")
first_forty = fileref.read(40)
print(first_forty)
fileref.close()

fileref = open("d:/code/data/emotion_words2.txt", "r")
num_lines = 0
for line in fileref:
   num_lines += 1
print(num_lines)
fileref.close()

print("relative path")
fileref = open("../../data/emotion_words2.txt", "r")
num_lines = 0
for line in fileref:
   num_lines += 1
print(num_lines)
fileref.close()