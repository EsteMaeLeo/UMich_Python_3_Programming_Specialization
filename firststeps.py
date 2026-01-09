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

print(type(17))
print(type("Hello World!"))
print(type(3.2))
print(type("17"))
print(type("3.2"))
print(type('This is a string.'))
print(type("And so is this."))
print(type("""and this."""))
print(type('''and even this...'''))
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
print("""This message will span
several lines
of the text.""")
print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello", 45)

print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note that the result is closer to zero

print("2345", int("2345"))        # parse a string to produce an int
print(17, int(17))                # int even works on integers
# print(int("23bottles")) result on error 
print(float("123.45"))
print(type(float("123.45")))
print(str(17))
print(str(123.45))
print(type(str(123.45)))

val = 50 + 5
print("the value is " + str(val))  
total_secs = 7684
hours = total_secs // 3600 #give integer part
secs_still_remains = total_secs % 3600
minutes = secs_still_remains // 60
sec_finally_remains = secs_still_remains % 60
print("Hdrs=", hours, "mins=", minutes, "secs=", sec_finally_remains)
#Expresions and statements

print(1 + 1 + (2 * 3))
print(len("hello"))
print(2 * len("hello") + len("goodbye"))
x = 2
y = 1
print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))

str_seconds = input("Enter the seconds you want to convert: ")
total_secs = int(str_seconds)
hours = total_secs // 3600 #give integer part
secs_still_remains = total_secs % 3600
minutes = secs_still_remains // 60
sec_finally_remains = secs_still_remains % 60
print("Hdrs=", hours, "mins=", minutes, "secs=", sec_finally_remains)