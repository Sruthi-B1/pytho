#Merge two dictionaries. 
d1={"jan":31,"feb":28,"march":31}
d2={"april":30,"may":31,"jun":30,"july":31}
print("dictionaries 1 : ",d1)
print("dictionaries 2 :",d2)
d1.update(d2)
print("After merging both dictionaries",d1)
