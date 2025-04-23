#Simple calculations on user data

#01
p,r,t=float(input("Enter the Principle")), float(input("Enter the Rate of Interest")), int(input("Enter the time period"))
si=(p*r*t)/100
print("The Simple Interest is:", si)
print("The Maturity Amount is:", si+p)

#02
l,b=float(input("Enter the length")), float(input("Enter the breadth"))
a=l*b
print("The Area of the Rectangle is:",a)

#03
a,b,c=int(input("Enter First num")), int(input("Enter Second num")), int(input("Enter Third num"))
av=(a+b+c)/3
print("The Average of the three numbers is:", av)

#04
s=int(input("Enter the value of the side"))
vol=a**3
print("The Volume of the Cuboid is:", vol)

#05
x,y=int(input("Enter the value of x")), int(input("Enter the value of y"))
print("The Product of the two numbers is: ", x*y)