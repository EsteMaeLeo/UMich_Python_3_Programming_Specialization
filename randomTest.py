greeting = "hello world!"

for char in greeting:
    if char == "h":
        char = "j"
#    print(char)
    
print(greeting)

p_phrase = "was it a car or a cat I saw"
lt=[]
r_phrase = ""
for letter in p_phrase:
    lt.append(letter)

print("1", lt)
lt.reverse()

s = "1 2 3 4 5"
int_list = [int(i) for i in s.split()]
# Output: [1, 2, 3, 4, 5]

int_list_map = list(map(int, s.split()))
# Output: [1, 2, 3, 4, 5]
print(int_list_map)

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
print(len(sports)-3)
print(sports[len(sports)-3:])
print(sports[-1])
print(sports[-len(sports)])
indx = -1*len(sports)
print(sports[indx])
print(p_phrase[-1])

sentence = "The water earth and air"
words = p_phrase.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)
print(result)

reversed_text = "".join(reversed(p_phrase))
print(reversed_text)

reversed_text = ""

# The first argument is “len(p_phrase) - 1”. That makes the range() list start on the last index  since list 
#indexes start at 0, you need to subtract one
#The third argument  the step. The default is 1, which adds one to the list every time (until it gets to the second argument, the stop)
#A step of -1 will simply make the list subtract one each time instead. So it will essentially make the range() 
#list go backwards
#The second argument is the stop, which determines where the range() list stops adding numbers to the list. It’s 
#important to note that it does not include the stop number itself. Since we’re counting downward, -1 would make the 
#list stop at 0.
j = 0
str1 = ""
p_phrase2 = p_phrase.lower()
for i in range(len(p_phrase2)-1, -1, -1):  # from last index down to 0
    reversed_text += p_phrase2[i]
    print(i)
    if p_phrase2[i] == p_phrase2[j]:
        str1 = str1 + p_phrase2[i]
    j = j + 1
print(reversed_text)
print(str1)
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
print(r_phrase)

str2 = ""
for char in p_phrase:
    str2 = char + str2
print(str2)
if str2 == p_phrase:
    print(True)
print(False)