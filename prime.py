n=int(input("Enter a number : "))
if(n==1):
    print(f"{n} is neither prime nor composite.")
else:
    for i in range(2,n):
        if(n%i==0):
            print(f"{n} is a composite number.")
            break
    else:
        print(f"{n} is a prime number.")
