# My Day 1 learnings Are:

# print() function.
print ("Hello World!") 
# Output Hello World!


# New line using \n
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")
# Output is as follows,
# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

#String Concatination
print ("Hello" + "Hemant")
# Output HelloHemant

print ("Hello" + " " + "Hemant")
# Output Hello Hemant

#To get the length of Input and print it.
print (len(input("What is your name? ")))

#The above can be done using variables quiet easily
name = input("What is your Name?\n")
length = len(name)
print ("Number of Characters in your name is " + length)

# Use of " " and ' '
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
print("Mind the indentation (spaces) in your code")


# Variable Manupulation example using swap of 2 Numbers using 3rd variable
a = input("a: ")
b = input("b: ")
####################################
c = a
a = b
b = c
####################################
print("a: " + a)
print("b: " + b)