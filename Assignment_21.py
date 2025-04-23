#more on loops and range

#01
n=int(input("Enter the value of n"))
print("The first N even natural numbers")
for e in range(2,2*n+1,2):
    print(e)

#02
n=int(input("Enter the value of n"))
print("The first N odd natural numbers")
for e in range(1,2*n,2):
    print(e)

#03
n=int(input("Enter the value of n"))
print("The squares of first N natural numbers")
for e in range(1,n+1,1):
    print(e**2)

#04
n=int(input("Enter the value of n"))
print("The cubes of first N natural numbers")
for e in range(1,n+1,1):
    print(e**3)

#05
print("The list of all the prime numbers in the range [15,45]")
for e in range(15,46):
    for i in range(2,e):
        if e%i==0:
            break
    else:
        print(e)