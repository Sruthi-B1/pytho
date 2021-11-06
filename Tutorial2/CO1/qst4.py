#count the occurences of each word in a line of text
sen = input("Enter the text :")
w= sen.split(' ')
c = {}
for w in w:                                                                                                                                                                                              
    c[w] = c.get(w, 0) + 1   
print("The word is ",sen, " and the no:of occurences of each word in a line of text is :",c)  