#count the words in a file
with open("f.txt","w") as aa:
    aa.write("hello this is python program, i'm Sruthimol biju")
count=0
aa=open("f.txt","r")
for l in aa:
    w=l.split()
    count=len(w)
print("number ofwords in file f is :",count)
aa.close()