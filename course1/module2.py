#String

st = 'Hello'
notes = "Cdefgabcdefgabc"
print(notes[0])
print(len(notes))
print(notes[2:5])
print(notes.count("c"))
print(notes.index("d"))

firstName = 'Franz'
print(firstName.upper()) #"uppercase"
print(firstName.lower()) #"uppercase"

fruit = "grape"
midchar = fruit[len(fruit)//2]
print(midchar)

composer = "      Franz Liszt"
splitComposer = composer.strip()
print(splitComposer)

parag = "Franz Liszt was a Hungarian composer, virtuoso pianist, conductor and teacher of the Romantic period. With a diverse body of work spanning more than six decades, he is considered to be one of the most prolific and influential composers of his era, and his piano works continue to be widely performed and recorded."
sentence = parag.split(" ")
print(sentence)
#list

myList = ['One',2,"Three"]
print(myList)

myHardware = []
print(myHardware)
myHardware = ["screw", "nail"]
print(myHardware)
myHardware.append("nut")
print(myHardware)

myTools=["screwDriver", "wrench"]
mySupplies = myHardware + myTools
print(mySupplies)
print(mySupplies[0])
print(mySupplies[2:4])

print(mySupplies[4])
mySupplies[4] = "screw"
print(mySupplies[4])
print(len(mySupplies))
print(mySupplies.count("screw"))

alist =  ["hello", 2.0, 5]
print(len(alist))
print(len(alist[0]))

singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])

fruit = "banana"
print(fruit[:3])
print(fruit[3:])

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

fruit = ["apple","orange","banana","cherry"]
print([1,2] + [3,4])
print(fruit+[6,7,8,9])

print([0] * 4)

a = "I have had an apple on my desk before!"
print(a.count("e"))
print(a.count("ha"))

z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))
print(z.count(4))
print(z.count("a"))
print(z.count("electron"))

music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))

song = "The rain in Spain..."
wds = song.split()
print(wds)

song = "The rain in Spain..."
wds = song.split('ai')
print(wds)

song = "The rain in Spain..."
wds = song.split('ai')
print(wds)

wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))



#Tuples 

print("tuples")
myTuple =('One',2,"Three")
myTuple2 =(100,) # create one item
print(myTuple)
print(type(myList))
print(type(myTuple))

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)

#***********
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
print(len(sports)-3)
print(sports[len(sports)-3:])

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = by + " " + az + io + "," + " " + qy
print(message)


l = ['w', '7', 0, 9]
m = l[1:2]
print(m)
print(type(m)) #list

l = ['w', '7', 0, 9]
m = l[1]#"string"
print(m)
print(type(m)) 

s1 = {1,2,3,4}
s2 = {4,5,6}
print(s1&s2)