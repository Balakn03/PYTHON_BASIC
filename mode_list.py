l=input().split()
l=[int(i) for i in l]
ls=[]
for i in l:
    c=0
    for j in l:
        if(i==j):
            c+=1
    ls.append(c)
maxi=max(ls)
d=dict(zip(l,ls))
print("The mode of the given list is ",end="")
for key,values in d.items():
    if values==maxi:
        print(key," ",end='')
