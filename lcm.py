a=int(input("a = "))
b=int(input("b = "))
c=max(a,b)
for i in range(c,a*b+1):
    if i%a==0 and i%b==0:
        print(i,"is the LCM of two numbers.")
        break
