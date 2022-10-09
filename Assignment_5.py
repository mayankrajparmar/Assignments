                        # Assignment - 5 : Operators
# 1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
num = int(input('Enter The Number: '))
num = int(num/10)
print('New value of a number is:',num)

# 2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
num = int(input('Enter The Number: '))
num = int(num%10)
print('Last digit from a given number is:',num)

# 3. Write a python script to swap data of two variables
number_1 = int(input('Enter The number_1: '))
number_2 = int(input('Enter The number_2: '))
number_1 , number_2 = number_2 , number_1
print('New value of a number_1 is:',number_1)
print('New value of a number_2 is:',number_2)

# 4. Write a python script to find x power y, where values of x and y are given by user
number = int(input('Enter The number: '))
power = int(input('Enter The power: '))
answer = number**power
print(f'Answer is: {answer}')

# 5. Write a python script which takes a three digit number from the user and displays only its first digit.
number = int(input('Enter the three digit number: '))
number = number//100
print('First digit of a number is:',number)

# 6. Write a python script which takes a three digit number from the user and displays only its middle digit
number = int(input('Enter the three digit number: '))
number = number//10
number = int(number%10)
print('Middle digit of a number is:',number)

# 7. Write a python script which takes a three digit number from the user and displays only its last digit.
number = int(input('Enter the three digit number: '))
number = int(number%10)
print('Last digit of a number is:',number)

# 8. Write a python script to use IN operator to display the data present in the list
list = [20,45,60,37,21]
number = int(input('Enter the number: '))
print(number in list)

# 9. Write a python script to use NOT IN operator to display the data not present in list
list = [20,45,60,37,21]
number = int(input('Enter the number: '))
print(number not in list)

# 10. Write a python script to use IS operator to display if both variables are the same object or not?
a = 10
b = 10
print(a is b)