student = {
    "David" : {"Programing" : 100, "English": 95},
    "William" : {"Programing" : 80, "English": 100},
    "John" : {"Programing" : 75, "English": 75}
}

print(student["David"]["English"])

student["Lex"] = {"Programing" : 80, "English": 100}
print("adding Lex... ", student)

print("key: ", student.keys())
print("values:  ", student.values())
print("Items: ", student.items())
print("to remove all use student.cler()")
print("Get: ", student.get("David"))

print("Pop: ", student.pop("David"))
print(student)