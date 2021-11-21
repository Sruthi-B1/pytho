#check whether two lists contain any common elements
l1=[4,6,7,8,9]
l2=[2,3,4,69,8]
s1=set(l1)
s2=set(l2)
s3=s1.intersection(s2)
print(s3)