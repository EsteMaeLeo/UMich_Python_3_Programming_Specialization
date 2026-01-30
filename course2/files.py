'''
open(filename,'r') Open a file called filename and use it for reading. This will return a reference to a file object.
open(filename,'w') Open a file called filename and use it for writing. This will also return a reference to a file object.
close filevariable.close() File use is complete.
'''

fileref = open("d:/code/data/data.txt", "r")
contents = fileref.read() # read all file
print(contents)
## other code here that refers to variable fileref
fileref.close()