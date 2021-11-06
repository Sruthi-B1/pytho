"""Get a string from an input string where all occurrences of first character replaced with
‘$’, except first character.
[eg: onion -> oni$n] """
str1= input("Enter the string : ")
ch = str1[0]
str1 = str1.replace(ch, '$')
str1 = ch + str1[1:]
print("The new string is : ",str1)