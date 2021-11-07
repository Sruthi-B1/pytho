#Find the sum of all items in a list
lst =[]
li = [44,30,1,71,40,91,111]
sum=0
for x in range(0,len(li)):
    sum = sum + li[x]
print("Sum of items in list = ",sum)