                      # Assignment-6: Decision Control
# 1. Write a python script to check whether a given number is positive or non-positive
num = int(input("Enter the number: "))
if num>0:
    print("Number is positive")
else:
    print("Number is non-positive")

# 2. Write a python script to check whether a given number is divisible by 5 or not
num = int(input("Enter the number: "))
if num%5==0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

# 3. Write a python script to check whether a given number is even or odd
print("Number is odd" if int(input("Enter the number: "))%2 else "Number is even")

# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
print('Enter two numbers:')
a,b = int(input()),int(input())
print(a if a>b else b)

# 5. Write a python script to print two given words in dictionary order
print('Enter two words:')
a,b = input(),input()
print((b,a) if a>b else (a,b))

# 6. Write a python script to check whether a given number is a three digit number or not.
num = int(input("Enter the number: "))
if 99<num<1000:
    print('given number is a three digit number')
else:
    print('given number is not a three digit number')

# 7. Write a python script to check whether a given number is positive, negative or zero.
num = int(input("Enter the number: "))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print("Number is zero")

# 8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
print('Enter the value of a,b and c of a quadratic equation:')
a,b,c = int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print('real & distinct roots')
elif d==0:
    print('real & equal roots')
else:
    print('imaginary roots')

# 9. Write a python script to check whether a given year is a leap year or not.
year = int(input("Enter the year number: "))
if year%400==0 or year%100!=0 and year%4==0:
    print('Leap Year')
else:
    print('Non Leap Year')

# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
print('Enter the value of first,second and third number:')
a,b,c = int(input()),int(input()),int(input())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>a:
    if b>c:
        print(b)
    else:
        print(c)
else:
    print(c)

# 11. Write a python script to take the month value in numeric format and display the number of days in it.
month = int(input('Enter month number: '))
if month in (1,3,5,7,8,10,12):
    print('31 Days')
elif month in (4,6,9,11):
    print('30 Days')
else:
    print('28 or 29 Days')

# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
x = complex(input('Enter the number: '))
print((x.real) if x.real>x.imag else (x.imag))