# Assignment-14: More on List

# 1. Write a Python script to create a list of first N natural numbers.
n = int(input("Enter the value of N: "))
l1 = []
for x in range(n):
    l1.append(x+1)
print(l1) 

# 2. Write a Python script to create a list of first N odd natural numbers.
n = int(input("Enter the value of N: "))
l1 = []
for x in range(n):
    l1.append(2*x+1)
print(l1)

# 3. Write a Python script to create a list of first N even natural numbers.
n = int(input("Enter the value of N: "))
l1 = []
for x in range(1,n):
    l1.append(2*x)
print(l1)

# 4. Write a Python script to find the greatest number in a given list of numbers.
li = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(max(li))

# 5. Write a Python script to find the smallest number in a given list of numbers.
li = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(min(li))

# 6. Write a Python script to calculate the sum of elements in a given list of numbers.
li = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(sum(li))

# 7. Write a Python script to remove all non int values from a list.
my_list = [5, 2, 1, True, 'abcdefg', 3, False, 4]
y = [x for x in my_list if type(x)!=int]
print(y)

# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
li = [2, 4, 6, 8, 10, 12, 14, 16, 18,2, 4, 6, 8, 10, 12, 14, 16, 18,5,4,2,10]
y = list(set(li))
print(y)

# 9. Write a Python script to print indices of all occurrences of a given element in a given list.
li = [2, 4, 5, 6, 8, 10, 12, 14, 16, 18]
for x in li:
    print(li.index(x),"--",x)

# 10. Write a python script to sort a list.
    li = [2, 4, 6, 8, 10, 12, 14, 16, 18,2, 4, 6, 8, 10, 12, 14, 16, 18,5,4,2,10]
print(sorted(li))