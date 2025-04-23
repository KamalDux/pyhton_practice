#Match

#01
x=int(input("Enter a value"))
match x:
    case x if x>99 and x<1000:
        print("Three digit number")
    case _:
        print("Not a three digit number")

#02
x=int(input("Enter a value"))
match x:
    case x if x>0:
        print("Positive number")
    case x if x<0:
        print("Negative number")
    case _:
        print("Zero")

#03
print("Welcome to menu driven program")
print("1.Odd-Even\n2.Non-positive\n3.Simple Interest\n4.Find roots of Quadratic Equation")
num=int(input("Enter your choice"))
match num:
    case 1:
        a=int(input("Enter a number"))
        print("Even" if a%2==0 else "Odd")
    case 2:
        a=int(input("Enetr a number"))
        if a>0:
            print("Positive")
        else:
            print("Non-positive")
    case 3:
        p,r,t=int(input("Enter P")), int(input("Enter R")), int(input("Enter T"))
        print("The simple interest is: ", p*r*t/100)
        print("The maturity amount is: ",p*r*t/100 + p)
    case 4: 
        a,b,c=int(input("Enter the value a")), int(input("Enter the value b")), int(input("Enter the value c"))
        d=b**2-4*a*c
        if d>0:
            print("Roots are real and distinct")
        elif d==0:
            print("Roots are real and equal")
        else:
            print("Roots are imaginery")
    case _:
        print("Wrong choice")

#04
a=eval(input("Enter a value/expression"))
match a:
    case a if type(a)==int:
        print("Monday")
    case a if type(a)==float:
        print("Tuesday")
    case a if type(a)==complex:
        print("Wednesday")
    case a if type(a)==bool:
        print("Thrusday")
    case _:
        print("No-day")

#05
a=input("Please enter a string")
match a:
    case a if a in "mysirg":
        print("One")
    case a if a in "education":
        print("Two")
    case a if a in "services":
        print("Three")
    case _:
        print("Invalid")