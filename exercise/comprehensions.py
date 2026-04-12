# new_list = [new_item for item in list if condition]
# new_list = [expression for item in list if condition]
# new_list = [expression if/else for item in list ]

doubles = []  
for x in range(1,11):
    doubles.append(x * 2)
    
print("Using loop: ", doubles)

doubles = [x * 2 for x in range(1,11)]
print("Using comprehension: ", doubles)