# Assignment-15: Strings


# 1. Write a python script to create a String in 3 different possible ways
a = "Mayank"
b = 'Mayank'
c = """Mayank"""
d = "\"Teacher's day\""
print(a,b,c,d,sep="\n")

# 2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
a = "iNeuron"
print(a[:6])

# 3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
a ="Hello Learners"
print(a[2:6:])

# 4. Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
a="Learning"
b=" Python"
print(a+b)

# 5. Write a python script to get the count of total number of characters in String a=“iNeuron”
a = "iNeuron"
print(len(a))   

# 6. Write a python script to reverse a String. (“iNeuron”)
a = "iNeuron"
print(a[::-1])

# 7. Write a python script to determine whether a string contains a specific substring.
full_string = "MysirG Education Services"
sub_string = "sir"
print("found substring in full_string" if sub_string in full_string else "Not found substring in full string")

# 8. Write a python script to check if a string contains only numbers.
a = "123456"
b = "iNeuron"
print(a.isnumeric())
print(b.isnumeric())

# 9. Write a python script to check if a string contains only characters of the alphabet.
a = "123456"
b = "iNeuron"
print(a.isalpha())
print(b.isalpha())

# 10. Write a python script to convert an integer to a string.
a = str(98745632145)
print(type(a))
