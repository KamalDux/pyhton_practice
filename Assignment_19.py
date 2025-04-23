#for loop

#01
s=input("Enter a string")
print("The string characters with their respective unicodes:")
for e in s:
    print(e, ord(e))

#02
s=input("Enter a string")
print("The string characters which are vowels:")
for e in s:
    if e in 'AEIOUaeiou':
        print(e)

#03
s=input("Enter a string")
print("The no. of string characters which are spaces:")
count=0
for e in s:
    if e==' ':
        count+=1
print(count)

#04
num=input("Enter a number")
s=''
print("The number of unique characters are:")
for e in num:
    if e not in s:
        s+=e
print(s)

#05
num=input("Enter a number")
count=0
print("the number of spaces in the given string is:")
for e in num:
    if e in '0123456789':
        count+=1
print(count)