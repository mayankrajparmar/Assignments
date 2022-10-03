                        # Assignment-4 : User Input Problems
# 1. Write a python script to take your name as input from the user and then print it.
name = input('Enter Your Name: ')
print(name)

# 2. Write a python script to take input from the user. Input must be a number.
a = int(input('Enter The Number: '))
print(type(a))

# 3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
a = int(input('Enter The First Number: '))
b = int(input('Enter The Second Number: '))
print('The Sum Of Two Numbers is:',a+b)

# 4. Write a python script which takes the radius from the user and display area of a circle.
from math import pi
r = float(input('Enter the radius of a circle: '))
print('Area of a circle is :',pi * r**2)

# 5. Write a python script to calculate the square of a number. Number is entered by the user.
x = int(input("Enter the number: "))
print('Square of a number is',x**2)

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f'The area of the triangle is {area}')

# 7. Write a python script to calculate average of three numbers, entered by the user
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
c = float(input('Enter third number: '))
avg = (a + b + c) / 2
print(f'The average of the number is {avg}')

# 8. Write a python script to calculate simple interest
p = float(input('Enter principal: '))
t = float(input('Enter time period: '))
r = float(input('Enter rate of interest: '))
si = (p * t * r)/100
print('The Simple Interest is', si)

# 9. Write a python script to calculate the volume of a cuboid.
l = float(input('Enter length: '))
b = float(input('Enter breadth: '))
h = float(input('Enter height: '))
print('Volume of a cuboid is: ',l*b*h)

# 10. Write a python script to calculate area of a rectangle
l = float(input('Enter length: '))
h = float(input('Enter height: '))
area = l*h
print(f'The area of the rectangle is {area}')