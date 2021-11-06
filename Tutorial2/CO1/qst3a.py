#Generate positive list of numbers from a given list of integers
l1=[]
n=int(input("Enter the limit of the list : "))
print("Enter",n," Numbers :")
for l in range(0,n):
    t=int(input())
    l1.append(t)
print("Old list : ",l1)
l2=[i for i in l1 if i>0]
print("New list : ",l2)