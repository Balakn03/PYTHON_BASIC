a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
lst=[a,b]
x=min(lst)
l=[]
for i in range(1,x+1,1):
    if a%i==0 and b%i==0 :
        l.append(i)
g=max(l)
print(f"The GCD of two numbers is {g}")
