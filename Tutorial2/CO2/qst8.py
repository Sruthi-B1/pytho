#Accept a list of words and return length of longest word.
def long_word(word_list):
    word_len=[]
    for word in word_list:
        word_len.append((len(word),word))
    
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
    
word=long_word(["my","name","is","sruthimol biju"])
print("\nThe longest word is: ",word[1])
print("\nand the length of '",word[1],"' is: ",word[0])