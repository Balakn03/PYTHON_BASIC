import random
n=int(input("Enter the number of digits (4 or 6) : "))
print("The OTP is ", end='')
for i in range(n):
    a=random.randrange(10)
    print(a,end="")
