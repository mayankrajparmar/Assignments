# Assignment-19: Functions


# 1. Write a python program to create a simple function which prints “MySirG” .
def func():
    print("MySirG")
func()  

# 2. Write a python program to create a function which expects two arguments and print them in the function body.
def func(a,b):
    print("value of first argv is: ",a)
    print("value of second argv is: ",b)
func(15,16)  

# 3. Write a python program to create a function which expects an unknown number of arguments.
def function(*t):
    Average = sum(t)/len(t)
    return Average
avg = function(10,20,30,40) 
print(avg)

# 4. Write a python program to create a function which expects kwargs arguments.
def function1(a,b,c,d):
    e = a+b+c+d
    return e
print("sum is",(function1(b=2,a=5,c=85,d=3)))

# 5. Write a python program to create a function which expects a list as an argument.
def func(*t):
    for k in t:
        print(k)
func([15,16,75,96])  

# 6. Write a python program to create a function that finds a maximum of four numbers.
def func(*t):
    for k in t:
        print(max(k))
func(eval(input("Enter commmas separted four value: "))) 


# 7. Write a python program to sum all the numbers in a list.
def func(*t):
    for k in t:
        print(sum(k))
func([15,16,75,96]) 

# 8. Write a python program to multiply all the numbers in a list.
def func(*t):
    result = 1
    for k in t:
        for j in k:
            result*=j
        return result
k = func([1,1,5,6]) 
print(k)

# 9. Write a python program to create a function to check whether a number falls in a given range.
def function2(a):
    if a > 50 and a <= 100:
        print("Number {} is in our range".format(a))
    else:
        print("Number is out of range")
function2(int(input("Enter the number in between our range: ")))  

# 10. Write a python program to create a function to check whether a given number is even or odd.
def even_odd(a):
    if a % 2 == 0:
        print("Number is even ")
    else:
        print("Number is odd ")
even_odd(int(input("Enter a number: ")))   