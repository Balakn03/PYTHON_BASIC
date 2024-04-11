def leapyear(n):
	if n%4==0 and n%100!=0 or n%400==0:
		return "leap year"
	else:
		return "Non-leap year"
n=int(input("Enter the year"))
print(leapyear(n))
