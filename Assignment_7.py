                        # Assignment-7: Match Case
# 1. Write a python script to display the number of days in a given month number
month = int(input('Enter month number: '))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print('31 Days')
    case month if month in (4,6,9,11):
        print('30 Days')
    case 2:
        print("28 Or 29 Days")
    case _:
        print("invalid monter number")

# 2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter Your Choice: "))
match choice:
    case 1:
        print("Enter two numbers")
        a,b = int(input()),int(input())
        c = a+b
        print("Addition is",c)
    case 2:
        print("Enter two numbers")
        a,b = int(input()),int(input())
        c = a-b
        print("Subtraction is",c)
    case 3:
        print("Enter two numbers")
        a,b = int(input()),int(input())
        c = a*b
        print("Multiplication is",c)
    case 4:
        print("Enter two numbers")
        a,b = int(input()),int(input())
        c = a/b
        print("Division is",c)
    case _:
        print("Invalid Input")


# 4. Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 - Experienced, Age above or equal 60 - Senior Citizen.

age = int(input("Enter the age: "))
match age:
    case age if age>0 and age<10:
         print("kid")
    case age if age<20:
        print("Teen")
    case age if age< 40:
        print("Young")
    case age if age <60:
        print("Experienced")
    case age if age>= 60:
        print("Senior Citizen")

# 5. Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.

num = int(input("Enter the number: "))
match num:
    case num if num%2==0:
            print("Saurabh Shukla")
    case num if num<0 and num%2!=0:
        print("Prateek Jain")
    case num if num >0 and num%2!=0: 
        print("Aditya Choudhary")

# 6.Write a python program to check whether a given string is a multiword string or single
# word string using match case statement

x = input("Enter the string: ").split()
y = len(x)
match y:
    case 1:
        print("single word")
    case _:
        print("multiword")

# 7.Write a python program to check whether a given number is positive, negative or zero using match case statement

num = int(input("Enter the number: "))
if num>0:
    y=1
elif num<0:
    y=-1
else:
    y=0
match y:
    case 1:
        print("Positive")
    case -1:
        print("Negative")
    case 0:
        print("zero")

# 8.Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second string in dictionary order using match case statement

s1,s2 = input("Enter string first: "),input("Enter string first: ")
match (s1,s2):
    case (s1,s2) if s1 == s2:
        print("Indentical Strings")
    case (s1,s2) if s1 < s2:
        print("{} comes before the {}".format(s1,s2))
    case (s1,s2) if s1 > s2:
        print("{} comes after the {}".format(s1,s2))    

# 9.Write a python script to check whether a given year is
# a. Non century leap year b. Century leap year c. Non century non leap year d. Century non leap year
year = int(input("Enter the year: "))
match year:
    case year if year%100!=0 and year%4==0:
        print("Non century leap year")
    case year if year%100==0 and year%400==0:
        print("Century leap year")
    case year if year%100!=0 and year%4!=0:
        print("Non century non leap year")
    case year if year%100==0 and year%400!=0: 
        print("Century non leap year")
    
# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday

s = input("what is your favorite colour?")
li = ["yellow","blue","orange","white","black","red"]
for colour in li:
    if colour in s:
        c = colour
        break 
else:
    c = "other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")