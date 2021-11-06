#Find gcd of 2 numbers. 
from fractions import gcd
num1 = int(input("Enter the First number : "))
num2 = int(input("Enter the second number : "))
print("GCD (",num1,",",num2,") is : "+str(gcd(num1,num2)))