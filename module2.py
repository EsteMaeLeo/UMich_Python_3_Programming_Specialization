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