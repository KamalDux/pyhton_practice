#loops again

#01
num=int(input("Enter the number to find the factorial of"))
fact=1
for e in range(1,num+1,1):
    fact*=e
print("The factorial of the given number is:",fact)

#02
num=int(input("Enter the number you want to count the digits of"))
count=0
while num:
    count+1
    num//=10
print("The number of the digits in the given number is",count)

#03
num=int(input("Enter the number you want the digit sum of"))
sum=0
while num:
    sum+=num%10
    num//=10
print("The sum of digits is: ",sum)

#04
nums=int(input("Enter the digit you want binary equivalent of"))
while nums:
    num=nums
    n=1
    ans=''
    while n<=num:
        n*=2
    if n>num:
        n//2
    while n:
        if n<=num:
            num-=n
            ans+='1'
        else:
            ans+='0'
        n//=2
    print("The equivalent binary converted string is: ",ans)
    nums-=1

#05
num=int(input("Enter the digit you want octal equivalent of"))
n=1
while n<=num:
    n*=8
if n>num:
    n/=8
ans=''
while n:
    r=0
    n_copy=n
    while n_copy<=num:
        num-=n_copy
        r+=1
    ans+=str(r)
    n//=8
print("The octal equivalent is: ",ans)