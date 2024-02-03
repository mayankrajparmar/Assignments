# Assignment-17: Set


# 1. Write a python program to store all the programming languages known to you using Set.
set = {"Python", "Django", "JavaScript", "SQL","Java","SQL","C", "Cpp"}

# 2. Write a python program to store your own information {name, age, gender, so on..}
set1 = {"Mayank",21,"Male","B-Tech"}

# 3. Write a python script to get the data type of a Set.
print(type(set1))

# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}
thisset = {"Java", "Python", "Django"}
for x in thisset:
    if x == "Python":
        print("Python element found")
        break    
else:
    print("Not found")

# 5. Write a python program to add items from another set to the current set. thisset =
# {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}
thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
thisset = thisset.union(secondset)
print(thisset)


# 6. Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
mylist2 = {x for x in mylist}
thisset = thisset.union(mylist2)
print(thisset)

# 7. Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}
thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.discard("SQL")
print(thisset)

# 8. Write a python program to delete the set completely.
thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.clear()
print(thisset)

# 9. Write a python program to loop through the set and print values
# thisset = {"Python", "Django", "JavaScript", “SQL”}
thisset = {"Python", "Django", "JavaScript", "SQL"}
for element in thisset:
    print(element)

# 10. Write a python program to find the maximum and minimum value in a set.
thisset = {10,20,30,40,50,60,70}
print(min(thisset))
print(max(thisset))