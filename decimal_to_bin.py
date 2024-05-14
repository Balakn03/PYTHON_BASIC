a=int(input("Enter the decimal = "))
t=a
s=''
while(a>0):
    i=a%2
    s=str(i)+s
    a//=2
print(f"{t} is the binary form of {s}.")
