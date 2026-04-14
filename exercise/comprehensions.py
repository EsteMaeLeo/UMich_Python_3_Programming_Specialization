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
new_string = "".join([ i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i for i in string_line])[1:] #remove the first empty space at beggining also remove N to n and I  to i
print(new_string)

# Create a list of 10 tuples containing movies and years
movies_list = [
    ("The Shawshank Redemption", 1994),
    ("The Godfather", 1972),
    ("The Dark Knight", 2008),
    ("Pulp Fiction", 1994),
    ("Schindler's List", 1993),
    ("The Lord of the Rings: The Return of the King", 2003),
    ("Fight Club", 1999),
    ("Forrest Gump", 1994),
    ("Inception", 2010),
    ("The Matrix", 1999)
]

pre2k = [title for (title, year) in movies_list if year < 2000]
print(pre2k)

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
cartesian_product = [(a1, b1) for a1 in a for b1 in b ]
print(cartesian_product)

options = ["any", "albany", "apple", "world", "hello", ""]

valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]
print(valid_strings)

valid_strings = []
for string in options:
    if len(string) <= 1:
        continue
    if string[0] != "a":
        continue
    if string[-1] != "y":
        continue
    valid_strings.append(string)
print(valid_strings)