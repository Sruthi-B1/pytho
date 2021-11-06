#Print out all colors from color-list1 not contained in color-list2.
lst1 = []
lst2 = []
print("Enter the Colours in list 1 : ")
for x in range(1,5):
    a = str(input())
    lst1.append(a)
print("Enter the Colours in list 2 :  ")
for x in range(1,5):
    a = str(input())
    lst2.append(a)   
print("List 1 : ",lst1)
print("List 2 : ",lst2)
s1=set(lst1) 
s2=set(lst2) 
print("The diffrence is : ",s1.difference(s2))