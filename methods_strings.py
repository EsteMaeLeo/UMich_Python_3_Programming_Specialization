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