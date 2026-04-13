# new_list = [new_item for item in list if condition]
# new_list = [expression for item in list if condition]
# new_list = [expression if/else for item in list ]


doubles = []  
for x in range(1,11):
    doubles.append(x * 2)
    
print("Using loop: ", doubles)

doubles = [x * 2 for x in range(1,11)]
print("Using comprehension: ", doubles)

fruits = ["apple", "banana", "cherry", "pinaple"]
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [-1, -2, -5, 3 , 5, 6, 8]
positive_num = [number for number in numbers if number > 0]
negative_num = [number for number in numbers if number < 0]
even_nums = [number for number in numbers if number % 2 == 0]
odd_numbs = [number for number in numbers if number % 2 == 1]
print(positive_num)
print(negative_num)
print(even_nums)
print(odd_numbs)

bits = [False, True, False, False, True, False, True]
new_bits = [ 1 if b == True else 0 for b in bits ]

print(bits)
print(new_bits)

string_line= "HelloMyNameIsChancleta"

new_string = [i for i in string_line]
print(new_string)
new_string = "".join([ i if i.islower() else " " + i for i in string_line])
print(new_string)