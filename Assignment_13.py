#More on Desicion Control

#01
a=int(input("Enter a number"))
print("Three digit number" if a>99 and a<1000 else "Not three digit number")

#02
a=int(input("Enter a number"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

#03
a,b,c=int(input("Enter the value of a")), int(input("Enter the value of b")), int(input("Enter the value of c"))
d=b**2-4*a*c
if d>0:
    print("Roots are positive and distinct")
elif d==0:
    print("Roots are positive and equal")
else:
    print("Roots are imaginery")

#04
a=int(input("Enter the year number"))
if a%4==0:
    if a%100:
        print("Leap year")
    else:
        print("False")
elif a%400:
    print("True")

#05
a,b,c=int(input("Enter a number")), int(input("Enter a number")), int(input("Enter a number"))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)