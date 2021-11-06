#display future leap year From current year to a final year entered by user
from datetime import date
today = date.today()
y=today.year
x=int(input("Enter the final year : "))
if y > x:
    print("Sorry! Invalid Year ")
else:
    print("Leap years between ", y," and ",x , "  are : " )
    while y <= x:
        if (y % 4) == 0:
            if (y % 100) == 0:
                if (y % 400) == 0:
                    print(y)
            else:
                print(y)
        y += 1

    
       


