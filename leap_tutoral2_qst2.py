from datetime import date
today = date.today()
y=today.year
x=int(input(print("Enter the final year : ")))
print("Leap years between ", y," and ",x , "  are : " )
while y < x:
    if (y % 4) == 0:
        if (y % 100) == 0:
           if (y % 400) == 0:
               print(y)
        else:
            print(y)
    y += 1

    
       


