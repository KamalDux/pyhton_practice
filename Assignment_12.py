#Decision Control

#01
a=int(input("Enter a number"))
print("Positive" if a>0 else "Non-positive")

#02
a=int(input("Enter a number"))
print("Divisble by 5" if a%5==0 else "Not-divisible by 5")

#03
a=int(input("Enter a number"))
print("Even" if a%2==0 else "Odd")

#04
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print(a if a>b else b)

#05
a=input("Enter the first string")
b=input("Enter the second string")
print(b +" "+a if a>b else a+" "+b)