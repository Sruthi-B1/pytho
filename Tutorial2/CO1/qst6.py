#Store a list of first names. Count the occurrences of ‘a’ within the list
name=["anu","sujith","sruthi","nadhana","adhidev"]
n=0
for x in name:
  n=n+x.count("a")
print("Number of 'a' in the list",name," is :",n)