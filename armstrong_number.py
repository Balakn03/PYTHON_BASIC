n=int(input("Enter a number : "))
temp=n
l=len(str(n))
s=0
while(n>0):
    i=n%10
    c=i**l
    s+=c
    n//=10
if(temp==s):
    print(f"{temp} is an armstrong number.")
else:
    print(f"{temp} is not an armstrong number.")

