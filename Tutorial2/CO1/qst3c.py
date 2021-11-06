# Form a list of vowels selected from a given word
w= input("Enter the word : ")
a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vl=[i for i in w if i in a]
print("The word is ",w, " and vowels in the word  are :",vl)