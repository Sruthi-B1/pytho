#Find biggest of 3 numbers entered
y = float('-inf')
for x in range (0,3):
    a = int(input("Enter the Number :  "))
    if a > y:
        y = a
print("Biggest number is : ", y)
