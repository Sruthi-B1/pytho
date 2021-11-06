#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
#to same value (c) whether any value occur in both
lst1 = ['6', '7', '2', '9','4','55','14','100']
lst2 = ['0', '2', '66', '3', '6']
sum1 = str(0)
sum2 = str(0)
if len(lst1) == len(lst2):
    print("Both list are of same length")
else:
    print("Two lists have diffrent  length") 
for x in lst1:
    sum1 = sum1 + x
for x in lst2:
    sum2 = sum2 + x
if sum1 == sum2:
    a = "Equal"  
else:
    a = "Not Equal"  
print(" Sum of two list are : ", a)  
for x in lst1:
    for y in lst2:
        if x == y:
            print(y," Occurs in both lst")