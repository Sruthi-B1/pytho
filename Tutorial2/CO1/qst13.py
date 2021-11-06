#Create a list of colors from comma-separated color names entered by user. Display first and last colors
lst = []
for x in range(0,4):
    colour = input("Enter the colour : ")
    lst.append(colour)
print("first and last colors are : ", lst[0], lst[-1] )