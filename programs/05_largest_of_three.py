a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if(a>=b) and (a>=c):
    Largest=a
elif(b>=a) and (b>=c):
    Largest=b
else:
    Largest=c
print("The Largest number is :",Largest)