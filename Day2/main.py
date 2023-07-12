# My Day 2 learnings Are:

# Datatypes - There are four types of datatypes in Python - String, Integer, Float, and Boolean.

# String Datatype is denoted within quotes - single(' ') or double(" ").
# Examples are "123", "&@Axexejwn" "Hello", 'Hello', etc.

# Subscript - Process of pulling a character from a string is called Subscript.

value = "Hello"[1]
print (value)
# Outpput is e

#Please note counting starts from 0, 1, 2, ...., n
print ("Hemant"[0])
# Output is H 
print ("Hemant"[1])
# output is e
# as so on....

# Integers and floats 
# Examples of Integers 1, 1874, 4774, 68, etc.
# In maths we donote large numbers seperated by commas (,). Example - 32,000
# In python we denote large numbers seperated by underscore (_). Example - 32_000
# Examples of Float 3.141, 10.999, 1133.00, etc.
# They are deonted without the quotes - single(' ') or double(" ").

# Boolean - these are True or False value (in cammel case)


num_char = len( input ("What is your name? "))
# Below print statement will throw error, as input() function is always string and len() function is always integer.
# We can not concatinate two different Datatypes.
# print ("Your name has " + num_char + " characters.")

# We use type() function to know the type of a variable.

print (type(num_char))
# Output is <class 'int'>

# To convert one data type to another we use following functions.
# str () - to convert to string.
# int () - to convert to integer.
# float () - to convert to float.

print (70 + int("10"))
# Output is 80
print (70 + int(110.99))
# Output is 180
print (str(70) + str(100))
# Output is 70100

print ("Your name has " + str(num_char) + " characters.")
# Output will be Your name has x characters. 
# Where x is length of input.

# Alternatevely we can use f-String to conatinate other datatypes to Strings.
print (f"Your name has {num_char} characters.")
# Output will be Your name has x characters. 
# Where x is length of input

score = 0
height = 1.8
isWinning = True

print (f"Your score is {score}, your height is {height}, and you are winning is {isWinning}.")
# Output will be Your score is 0, your height is 1.8, and you are winning is true.


# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")

a = two_digit_number[0]
b = two_digit_number[1]

print (int(a) + int(b))


# Mathemetical Operations - Addition (+), substraction (-), Multiplication (*), Devision (/), and exponential (**).

print (10 + 5)
# Output 5
print (10 - 5)
# Output is 5
print (10 * 5)
# Output is 50
print (10 / 5)
# Output is 2.0
# Division always produce Float Datatype.
# To get integer of Devision we can use //
print (10 // 5)
# Output is 2
print (10 ** 5)
# Output is 100000
# It denotes 10 raise to the power 5 i.e (10 * 10 * 10 * 10 * 10).

# Python follows PEMDAS rules whch stands for Parentheses, Exponents, Multiplication and Division (same level), and Addition and Subtraction (same level).
# In python Multiplication and Division, and Addition and Subtraction are treated as same level.
# Therefore for Multiplication and Division, and Addition and Subtraction python starts calculation from Left to Right. 
# Therefore use Parentheses if you want the calcuation in specific order.
print (3 * 3 + 3 / 3 - 3)
# Output is 7.0
# To understand operation (3 * 3 + 3 / 3 - 3) = (9 + 3 / 3 - 3) = (9 + 1 - 3) = (10 - 3) = 7.0
print (3 / 3 - 3 * 3 + 3)
# Output is -5.0
# To understand operation (3 / 3 - 3 * 3 + 3) = (1 - 3 * 3 + 3) = (1 - 9 + 3) = (-8 + 3) = -5.0

# round() function - Used to round off a float datatype variable.
print (8 / 3)
# Output is 2.66666666
print (round(8/3))
# Output is 3
print (round((8/3), 3))
# This will round off till 3 decimal places
# Output is 2.667

# format() function - Used to roundoff/foramt float numbers.
print (5 / 2)
# Output is 2.5
print (round((5/2), 3))
# Here the output will be still 2.5 
# We can use format function to get output as 2.500
print ("{:.3f}".format(5/2))
# Output is 2.500
print ("{:.5f}".format(5/2))
# Output is 2.50000


# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#print (type(height))
#print (type(weight))

h = float(height)
w = int(weight)
#print (type(h))
#print (type(w))

BMI = int(w / (h ** 2))
print (BMI)

# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

age = input("What is your current age? ")

left = 90 - int(age)

days = left * 365
weeks = left * 52
months = left * 12

print (f"You have {days} days, {weeks} weeks, and {months} months left.")