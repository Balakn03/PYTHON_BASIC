a=int(input("Enter the Binary form = "))
t=str(a)
l=len(str(a))
t=t[::-1]
s=0
for i,j in enumerate(str(t)):
    p=int(j)*(2**i)
    s+=p
print(s)

