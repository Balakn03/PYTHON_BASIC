l=input("Enter the string : ")
for i in range(ord("a"), ord("z")+1):
    if chr(i) not in l:
        print("The given string is a non-panagram.")
        break
else:
     print("The given string is a panagram.")

