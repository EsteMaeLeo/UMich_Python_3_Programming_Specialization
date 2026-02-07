#upper Returns a string in all uppercase
#lower returns a string in all lowercase
#count returns the number of occurrences of item
#index Returns the leftmost index where the substring item is found and causes a runtime error if item is not found
#strip Returns a string with the leading and trailing whitespace removed
#replace Replaces all occurrences of old substring with new
print("Non-mutating Methods on strings")
ss = "Hello World"
upper = ss.upper()
print("Upper variable ss ", upper)
tt = ss.lower()
print("Lower variable ss ",tt)
ss = "    Hello, World    "

els = ss.count("l")
print("Coun L in Hello World: ",els)
print(ss)
print("Strip spaces on ss: ***"+ss.strip()+"***")

news = ss.replace("o", "***")
print("Resplace o with ***: ", news)

food = "banana bread"
print(food.upper())

s = "python rocks"
print("""Result of s[1]*s.index("n") """, s[1]*s.index("n"))
print("******************************************************")
print("""printing format string with substitutions {} .format()""")
print("*******before readble code*******")
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))
print("*******after readble code*******")
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))
print("*******using float giving how many decimals*******")    
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)
print("******************************************************")
#use an f-string, we must type the character “f” before the string content. We can then enter expressions 
#within the string between curly braces ({}). Whenever the python interpreter encounters curly braces inside an 
#f-string, it will evaluate the expression and substitute the resulting value into the string.
#We can use almost any expression inside the braces. It can be: a value; a variable that contains or references a value;
# an arithmetic expression; a string expression; a method call that returns a value such as a string or a number.
print("f-strings")
name = "Rodney Dangerfield"
score =  86.50
print("Hello {}. Your score is {}.".format(name, score))
print(f"Hello {name}. Your score is {score}.")

first_name = "Peter"
last_name = "Huang"
score = 96.75
print(f"Hello {'Peter' + ' ' + 'Huang'}. Your score is {90 + 6.75}.")

first_name = "Peter"
last_name = "Huang"
score = 96.75
print(f"Hello {first_name} {last_name}. Your score is {score}.")

first_name = "Peter"
last_name = "Huang"
score = 55.75
print(f"Hello {first_name} {last_name}. Your score is {max(score, 60)}.")

first_name = "Peter"
last_name = "Huang"
score = 96.75
print(f"Hello {first_name} {last_name}. Your score is {score:.1f}.")
print(f"Hello {first_name} {last_name}. Your score is {max(score, 60):.1f}.")

print("{} {}".format("{I need braces.}", "{I also need braces.}"))

s = "I saw the movie, Mary Poppins Returns, and I thought it was great."
print(s)
# all the expressions
r_count = s.count("r")
print("""r_count = s.count("r")""", r_count)
all_case_r_count = s.lower().count("r")
print("Len string s: ", len(s))
print("""all_case_r_count = s.lower().count("r")""", all_case_r_count)
r_precentage = all_case_r_count/len(s) * 100

# use mostly variables inside f-strings or format()
first_str = f"The number of r characters: {r_count}."
second_str = "The percentage of r characters (upper or lower case): {:.2f}%.".format(r_precentage)

# display
print( first_str + " " + second_str)

lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
print(lst)
lst.remove('pluto')
first_three = lst[:3]
print(first_three)
print("Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.")
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
print(sports)
sports.insert(2, "horseback riding")
print(sports)

print("Write code to take ‘London’ out of the list trav_dest.")
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
print(trav_dest)
trav_dest.remove("London")
print(trav_dest)

print("Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.")
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
print(trav_dest)
trav_dest.append("Guadalajara")
print(trav_dest)

x = ["dogs", "cats", "birds", "reptiles"]
y = x
print(id(y))
print(id(x))
x += ['fish', 'horses']
print(id(y))
print(id(x))
print(x)
print(y)
y = y + ['sheep']
# the behavior of obj = obj + object_two is different than obj += object_two when obj is a list. The first 
#version makes a new object entirely and reassigns to obj. The second version changes the original object so that 
#the contents of object_two are added to the end of the first.
print(id(y))
print(id(x))
print(x)
print(y)
#

sent = "The mall has excellent sales right now."
print(sent)
wrds = sent.split()
print(wrds)
wrds[1] = 'store'
print(wrds)
new_sent = " ".join(wrds)
print(new_sent)