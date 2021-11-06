#Accept a file name from user and print extension of that.
filename = input("Enter the Filename = ")
extension = filename.split(".")
print ("The extension of the file is : " + repr(extension[-1]))