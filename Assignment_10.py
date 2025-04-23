#Operators

#01
a=int(input("Enter a number"))
a//=10
print("The number without the last digit is: ", a)

#02
a=int(input("Enter a number"))
a%=10
print("The number's last digit is: ", a)

#03
a,b=int(input("Enter the first number")),int(input("'Enter the second number"))
a=a+b
b=a-b
a=a-b
print("The swapped values are: ",a," ",b)

#04
a=int(input("Enter a three digit number"))
a//=10
a//=10
print("Thee first digit is: ",a)

#05
a=int(input("Enter a three digit number"))
a//=10
a%=10
print("Thee middle digit is: ",a)