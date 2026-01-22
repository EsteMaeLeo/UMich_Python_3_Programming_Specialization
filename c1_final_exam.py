#Below are a set of scores that students have received in the past semester. Write code to determine 
#how many are 90 or above and assign that result to the value a_scores.
print("Question #1")
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
lst_scores = scores.split(" ")
print(scores)
print(lst_scores)
a_scores = []
for score in lst_scores:
    if int(score) >= 90:
        a_scores.append(int(score))
print(a_scores)

a_scores = 0
for score in lst_scores:
    if int(score) >= 90:
        a_scores = a_scores + 1
print(a_scores)

#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. Only 
#the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should 
#be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the 
#list stopwords. For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
print("******************************************************")
print("Question #2")
acro = ""
lst_org = org.split(" ")
for word in lst_org:
    if not(word in stopwords):
        acro = acro + word[0].upper()
print(acro)
