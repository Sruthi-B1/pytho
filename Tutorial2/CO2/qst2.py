#Generate Fibonacci series of N terms
n=int(input("Enter The Limit:"))
f=0                                         
s=1
if n<=0:
    print("The requested series is",f)
else:
        print(f)
        print(s)
        for x in range(2,n):
            next=f+s                           
            print(next)
            f=s
            s=next