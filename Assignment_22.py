#loops

#01
sum=0
for e in range(1,int(input("Enter the value of n"))+1,1):
    sum+=e
print("The sum is: ",sum)

#02
sum=0
for e in range(1,int(input("Enter the value of n"))+1,1):
    sum+=(e**2)
print("The sum of the squares is: ",sum)

#03
sum=0
for e in range(1,int(input("Enter the value of n"))+1,1):
    sum+=(e**3)
print("The sum of the cubes is: ",sum)

#04
sum=0
for e in range(1,2*int(input("Enter the value of n")),2):
    sum+=e
    print(e)
print("The sum of the first n odd natural numbers is: ",sum)

#05
sum=0
for e in range(2,2*int(input("Enter the value of n"))+2,2):
    sum+=e
    print(e)
print("The sum of the first n even natural numbers is: ",sum)