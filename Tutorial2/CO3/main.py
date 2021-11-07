from graphics.graphics3D import cuboid
from graphics.circle import *
import graphics.rectangle
from graphics.graphics3D import sphere
l = int(input("Enter the length of cuboid"))
b = int(input("Enter the breath of cuboid"))
h = int(input("Enter the height of cuboid"))
x = int(input("Enter the radius of circle"))
a = int(input("Enter the length of rectangle"))
c = int(input("Enter the breath of rectangle"))
y = int(input("Enter the radius of Sphere"))

print("Area of Rectangle : "+str(graphics.rectangle.getArea(a,c)))
print("Area of Cuboid : "+str(cuboid.getArea(l,b,h)))
print("Area of Circle : "+str(getArea(x)))
print("Perimeter of Cuboid : "+str(cuboid.getPerimeter(l,b,h)))
print("Perimeter of Rectangle : "+str(graphics.rectangle.getPerimeter(a,c)))
print("Perimeter of Circle : "+str(getPerimeter(x)))
print("Area of sphere : "+str(sphere.getArea(y)))
print("Perimeter of sphere : "+str(sphere.getPerimeter(y)))