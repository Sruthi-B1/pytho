#list ordinal values of each elements of a word to get ordinal values
x = input("Enter the word : ")
b=[ord(i) for i in x]
print("Word is ",x, "and ordinal value of each element is :",b)