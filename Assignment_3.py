                         # Assignment-3: Type Conversion
# 1. Write a python script to convert a number into str type.
a = 10
print(type(str(a)))

# 2. Write a python script to print Unicode of the character ‘m’
print(ord('m'))

#  3. Write a python script to print character representation of a given unicode 100.
print(chr(100))

# 4. Write a python script to print any number and its binary equivalent
x = 14
print(bin(x))

# 5. Write a python script to print any number and its octal equivalent.
x = 14
print(oct(x))

# 6. Write a python script to print any number and its hexadecimal equivalent.
x = 14
print(hex(x))

# 7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
a = 0b1100101
print(a)

# 8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
a = 0x2F
print(oct(a))

# 9. Write a python script to store an octal number 125 in a variable and print it in binary format.
a = 0o125
print(bin(a))

# 10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format
print(bin(0o25) + bin(0x39))