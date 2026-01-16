x = True
y = False
print(x or y)
print(x and y)
print(not x)

x = 5
print(x > 0 and x < 10)

n = 25
print(n % 2 == 0 or n % 3 == 0)

total_weight = int(input('Enter total weight of luggage:'))
num_pieces = int(input('Number of pieces of luggage?'))

if num_pieces != 0 and total_weight / num_pieces > 50:
   print('Average weight is greater than 50 pounds -> $100 surcharge.')

print('Luggage check complete.')

print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')

print('a' in 'a')
print('apple' in 'apple')
print('' in 'a')
print('' in 'apple') #that a string is a substring of itself, and the empty string is a substring of any other string.
