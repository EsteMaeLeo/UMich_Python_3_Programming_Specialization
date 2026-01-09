print("Hello, World!")
print("Operators")
print(10 + 5)
print(10 - 5)
print(9 / 5)
print(9 // 5)   ##If you want truncated division, which ignores the remainder,  use the // operato
print(10 % 3)
print(10 * 5)
print(10 ** 5)
print( (10+20) / 2 )
print(18.0 // 4)
print(18 % 4)
print(2 ** 3 ** 2)     # the right-most ** operator gets done first!
print((2 ** 3) ** 2)   # use parentheses to force the order you want!
'''
Function calls
'''
def square(x):
   return x * x

def sub(x, y):
   return x - y

print(square(3))
print(sub(6, 4))
print(sub(5, 9))
print(square(3) + 2)
print(sub(square(3), square(1+1)))
print(square)

'''Data Types'''
print("Data Types")