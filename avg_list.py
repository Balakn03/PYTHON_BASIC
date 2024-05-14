inp=input("Enter the list : ")
lst=inp.split()
lst=[int(i) for i in lst]
s,n=0,0
for i in lst:
    s+=i
    n+=1
m=s/n
print(f"The average of the given list is {m}")
