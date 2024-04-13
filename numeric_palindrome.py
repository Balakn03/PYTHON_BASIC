n=int(input("Enter a number : "))
s=0
t=n
while(n>0):
    i=n%10
    s=(s*10)+i
    n//=10
if t==s:
    print(f"{t} is palindrome.")
else:
    print(f"{t} is not palindrome.")

