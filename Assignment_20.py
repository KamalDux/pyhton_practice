#for loop and range

#01
print("The first 10 multiples of 5")
for e in range(5,55,5):
    print(e)

#02
n=int(input("Enter the value of n"))
print("The first 10 multiples of n")
for e in range(n,n*11,n):
    print(e)

#03
n=int(input("Enter the value of n"))
m=int(input("Enter the value of m"))
print("The first m multiples of n")
for e in range(n,n*(m+1),n):
    print(e)

#04
n=int(input("Enter the value of n"))
print("The first 10 multiples of n in reverse order")
for e in range(n*10,0,-n):
    print(e)

#05
n=int(input("Enter the value of n for printing it's table"))
for e in range(n,n*11,n):
    print(e)