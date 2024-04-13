inp=input("Enter the list : ")
lst=inp.split()
lst=[int(i) for i in lst]
lst.remove(max(lst))
x=max(lst)
print(f"{x} is the second largest number.")

