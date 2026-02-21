import csv
fileconnection = open("../test/reduced_olympics.csv", "r")
reader = csv.reader(fileconnection)
rows = list(reader)
headers = rows[0]

print(headers)
#rows[1:] avoid the first column
for row_vals in rows[1:]:
    if row_vals[0] != "NA":
        print(f"{row_vals[0]} : {row_vals[1]} : {row_vals[2]}")

#Elegant
print()
print("Elegant way with open")
print()
with open("../test/reduced_olympics.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(headers)
    #rows[1:] avoid the first column
    for row_vals in reader:
        if row_vals[0] != "NA":
            print(f"{row_vals[0]} : {row_vals[1]} : {row_vals[2]}")