'''
fileconnection = open("../grade.cvs", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))
'''

n = [0] * 12
for i in range(1,13):
    n[i-1] = i *12
outfile = open("../test/Multiples of 12", "w")
for j in range(0, len(n)):
    outfile.write(str(j+1) + ',' + str(n[j]))
    # +1 to j since the array starts at 0 and we start counting at 1
    outfile.write('\n')
outfile.close()

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("../test/reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

outfile = open("../test/split_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = ','.join([olympian[0], str(olympian[1]), olympian[2]])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()