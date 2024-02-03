# Assignment-11: loops

# 1. Write a python script to calculate sum of first N natural numbers
n=int(input("Enter the number : "))
s=0
for i in range(1,n+1):
    s+=i
print("sum of first ",n," natural numbers are : ",s)

# 2. Write a python script to calculate sum of squares of first N natural numbers
n=int(input("Enter the number : "))
s=0
for i in range(1,n+1):
    s+=i**2
print("Sum of sqaure of first ",n," natural numbers are : ",s)

# 3. Write a python script to calculate sum of cubes of first N natural numbers
n=int(input("Enter the number : "))
s=0
for i in range(1,n+1):
    s+=i**3
print("Sum of cube of first ",n," natural numbers are : ",s)

# 4. Write a python script to calculate sum of first N odd natural numbers
n=int(input("Enter the number : "))
s=0
for i in range(2*n-1,0,-2):
    s+=i
print("sum of first ",n," odd natural numbers are : ",s)

# 5. Write a python script to calculate sum of first N even natural numbers
n=int(input("Enter the number : "))
s=0
for i in range(2*n,0,-2):
    s+=i
print("sum of first ",n," even natural numbers are : ",s)

# 6. Write a python script to calculate factorial of a given number
from re import I

n=int(input("enter the number that factorial you want to calculate : "))
f=1
for i in range(1,n+1):
    f*=i
print("factorial of ",n," are : ",f)

# 7. Write a python script to count digits in a given number
n=int(input("enter the number : "))
j=0

while n:
    j+=1
    n=n//10
print("total numbers of digits in given number are : ",j)

# 8. Write a python script to calculate sum of digits of a given number
n=int(input("Enter the number : "))
s=0
while n:
    s+=n%10
    n=n//10
print("sum of digits of a given number : ",s)

# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
n=int(input("Enter the decimal number : "))
x=n
lis=[]
while n:
    r=n%2
    lis.append(r)
    n=n//2
lis.reverse()
s=0
for i in lis:
    s=i+s*10

print("The binary of the ",x," are : ",s)

# 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
n=int(input("Enter the number : "))
x=n
lis=[]
while n:
    r=n%8
    lis.append(r)
    n=n//8
lis.reverse()
s=0
for i in lis:
    s=i+s*10

print("The octal equivalent of ",x," decimal number are : ",s)