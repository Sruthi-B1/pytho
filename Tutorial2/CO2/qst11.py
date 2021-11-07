#Write lambda functions to find area of square, rectangle and triangle.
square=lambda a:a*a
length=int(input("Enter dimension of square:"))
print("Area of square=",square(length))
rectangle=lambda a,b:a*b
length=int(input("Enter length of rectangle:"))
breadth=int(input("Enter breadth rectangle:"))
print("Area of rectangle=",rectangle(length,breadth))
triangle=lambda b,h:0.5*b*h
base=int(input("Enter  length of triangle:"))
height=int(input("Enter height of triangle:"))
print("Area of triangle=",triangle(base,height))