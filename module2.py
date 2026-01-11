#String

st = 'Hello'
notes = "cdefgabcdefgabc"
print(len(notes))
print(notes[2:5])
print(notes.count("c"))
print(notes.index("d"))

firstName = 'Franz'
print(firstName.upper()) #"uppercase"
print(firstName.lower()) #"uppercase"

composer = "      Franz Liszt"
splitComposer = composer.strip()
print(splitComposer)

parag = "Franz Liszt was a Hungarian composer, virtuoso pianist, conductor and teacher of the Romantic period. With a diverse body of work spanning more than six decades, he is considered to be one of the most prolific and influential composers of his era, and his piano works continue to be widely performed and recorded."
sentence = parag.split(" ")
print(sentence)
#list

myList = ['One',2,"Three"]
print(myList)

#Tuples 
myTuple =('One',2,"Three")
myTuple2 =(100,) # create one item
print(myTuple)
print(type(myList))
print(type(myTuple))