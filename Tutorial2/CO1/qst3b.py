#Square of N numbers 
l1=[]
n=int(input("Enter the limit of the list : "))
print("Enter",n," Numbers :")
for l in range(0,n):
    t=int(input())
    l1.append(t)
print("Old list : ",l1)
l2=[i  **2 for i in l1 ]
print("New list : ",l2)