#Construct following pattern using nested loop
rows = int(input("Enter the number of steps required: "))  
   
for i in range(0, rows):   
    for j in range(0, i + 1):  
        print("*", end=' ')   
    print(" ")  

for i in range(rows , 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ") 