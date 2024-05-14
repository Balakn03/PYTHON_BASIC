l=input().split()
l=[int(i) for i in l]
l.sort()
n=len(l)-1
e=int(n/2)
o=int((n/2)-0.5)
if (n%2==0):
    median = l[e]
else:
    median = (l[o] + l[(o+1)]) / 2
print(f"The median of the list is {median}")
