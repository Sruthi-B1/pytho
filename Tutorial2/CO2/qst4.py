"""Generate a list of four digit numbers in a given range with all their digits even and the
number is a perfect square"""
u=int(input("Enter the upper limit="))
l=int(input("Enter the lower limit="))
li=[]
li1=[]

for x in range(l, u + 1):
    if x % 2 == 0:
        li.append(x)

for y in li:
    for z in range(1,y):
          if (z*z) ==y:
             li1.append(y)
print(li1)