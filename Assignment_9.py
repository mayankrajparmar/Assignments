# Assignment-9: While Loop

# 1. Write a python script to print MySirG N times on the screen
n = int(input("Enter the number: "))
i = 1
while i<=n:
    print("MySirG")
    i+=1

# 2. Write a python script to print first N natural numbers
n = int(input("Enter the number: "))
i = 1
while i<=n:
    print(i,end=" ")
    i+=1

# 3. Write a python script to print first N natural numbers in reverse order
n = int(input("Enter the number: "))
i = 1
while i<=n:
    print(n-i+1,end=" ")
    i+=1

# 4. Write a python script to print first N odd natural numbers
n = int(input("Enter the number: "))
i = 1
while i<=n:
    print(2*i+1,end=" ")
    i+=1

# 5. Write a python script to print first N odd natural numbers in reverse order
n = int(input("Enter the number: "))
i = n
while i>=1:
    print(2*i+1,end=" ")
    i-=1

# 6. Write a python script to print first N even natural numbers
n = int(input("Enter the number: "))
i = 1
while i<=n:
    print(2*i,end=" ")
    i+=1

# 7. Write a python script to print first N even natural numbers in reverse order
n = int(input("Enter the number: "))
i = n
while i>=1:
    print(2*i,end=" ")
    i-=1

# 8. Write a python script to print squares of first N natural numbers
n = int(input("Enter the number: "))
i = 1
while i<=n:
    print(i**2,end=" ")
    i+=1

# 9. Write a python script to print cubes of first N natural numbers
n = int(input("Enter the number: "))
i = 1
while i<=n:
    print(i**3,end=" ")
    i+=1

# 10. Write a python script to print first 10 multiples of N
n = int(input("Enter the number: "))
i = 1
while i<=10:
    print(n*i,end=" ")
    i+=1
