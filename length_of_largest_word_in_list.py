inp=input("Enter the list : ")
lst=inp.split()
lst=[str(i) for i in lst]
l=[]
for i in lst:
    x=len(i)
    l.append(x)
print(f"{max(l)} is the length of the longest word in the list. ")
