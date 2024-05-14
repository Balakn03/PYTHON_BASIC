a=list(map(int, input("Enter the list(a) : ").split()))
b=list(map(int, input("Enter the list(b) : ").split()))
c=[]
for i in a:
    for j in b:
        if i==j and i not in c:
            c.append(i)
print(f"The common elements in the list are {c}.")

