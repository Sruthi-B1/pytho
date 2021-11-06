#Create a string from given string where first and last characters exchanged. [eg: python -> nythop] 
str1= input("Enter the string : ")
print("The new string is : ",str1[-1:] + str1[1:-1] + str1[:1])
