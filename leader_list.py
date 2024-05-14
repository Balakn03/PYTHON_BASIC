lst=input("Enter the list : ").split()
lst=[int(i) for i in lst]
leader=[]

for i in range(len(lst)):
    for j in range(i+1,len(lst),1):
        if lst[j]>lst[i]:
            break
    else:
        leader.append(lst[i])
print(leader)
