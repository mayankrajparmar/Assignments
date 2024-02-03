# Assignment-12: More on loops


# 1. Write a python script to reverse a number.
n=int(input("Enter the number : "))
x=n
s=0
while n:
    r=n%10
    s=r+s*10
    n=n//10
print("The reverse of the ",x, " are : ",s)

# 2. Write a python script to check whether a given number is Prime or not
num=int(input("enter the number : "))
check=num//2
n=0
for i in range(2,check+1):
    if(num%i==0):
        
        print(num,"  is not primary number ")
        break
else:
    print(num," is a primary number ")

# 3. Write a python script to print all Prime numbers under 100
print("All primary number under 100 are : ")

for i in range(1,100+1):
    n=1
    for j in range(2,i//2+1):
        if(i%j==0):
            n=0  
    if n==1:
         print(i,end=" ") 

# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))

print("Prime numbers between ",a," and ",b," are : ")
for i in range(a,b+1):
    n=1
    for j in range(2,i//2+1):
        if(i%j==0):
            n=0
    if n==1:
        print(i,end=" ")

# 5. Write a python script to find next prime number of a given number
def nextprime(n):
    while True:
        n+=1
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            return n

n=int(input("Enter the prime number : "))

print("Next prime number are : ",nextprime(n))

# 6. Write a python script to print first N prime numbers
def nextprime(n):
    while True:
        n+=1
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            return n
def primegenerator(n):
    num,count=1,1
    # for i in range(n):
    #     p=nextprime(num)
    #     num=p
    #     yield p
    while count<=n:
        num=nextprime(num)
        yield num
        count+=1

n=int(input("Enter the number : "))
print("first ",n," prime numbers are : ")
for i in primegenerator(n):
    print(i,end=" ")

# 7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
print("Enter the two pair of number to check weather they are co-prime or not : ")

a,b=int(input()),int(input())
m=min(a,b)
for i in range(2,m):
        if(a%i==0 and b%i==0):
            flag=0
            print(a,b," are not co-prime numbers ")
            break
else:
        print(a,b,"are co-prime numbers")

# 8. Write a python script to print first N terms of a Fibonacci series
def fibonacci(n):

    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)   
n=int(input("Enter the value of n to print first n terms of fibonaccir series "))
print("First ",n,"  terms of fibonacci series are : ")

for i in range(n):
    print(fibonacci(i))

# 9. Write a python script to calculate LCM of two numbers
print("Enter the two numbers")
a=int(input("1st number "))
b=int(input("2nd number "))
c=max(a,b)
for i in range(c,a*b+1):
    if i%a==0 and i%b==0:
        print("LCM of ",a," and ",b," are : ",i)
        break

# 10. Write a python script to calculate HCF of two numbers
print("Enter the two numbers")
a=int(input("1st number "))
b=int(input("2nd number "))
c=min(a,b)
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        fac=i
print("HCF of ",a," and",b," are : ",fac)