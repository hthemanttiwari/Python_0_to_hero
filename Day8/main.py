# My Day 8 learnings Are:


# We can create our own functions.
# Syntax for the same is -

# Step 1 - Defining Function -
# def my_function():
#      First Do this
#      Than do this
#      Finally do this

# Step 2 - Calling function -
# my_function()

# Example -
def my_function():
    print("Hello")
    print("Bye")

# To call function
my_function()

# Here the ouptut will be
# Hello
# Bye


# Create a function called greet(). 
def greet():
    print("Hi")
    print("Hemant")
    print("Aman")

# Call the greet() function and run your code.
greet()

# Here the ouptut will be
# Hi
# Hemant
# Aman


# Function that allows input
def greet_with_name(name):
    print(f"Hi {name}")
    print(f"How do you do? {name}")

# Calling Function
greet_with_name("Hemant")

# Here the ouptut will be
# Hi Hemant
# How do you do? Hemant


# Function with more than 1 input
def greet_with(name, location):
    print(f"Hi {name}")
    print(f"What is it like in {location}?")

greet_with("Hemant", "Mumbai")

# Here the ouptut will be
# Hi Hemant
# What is it like in Mumbai?


# Always 1st peramenter will have 1st argument and 2nd will have 2nd argument.
greet_with("Mumbai", "Hemant")

# Here the ouptut will be
# Hi Mumbai
# What is it like in Hemant?


# To avoid this we can do
greet_with(location = "Mumbai", name = "Hemant")

# Here the ouptut will be
# Hi Hemant
# What is it like in Mumbai?



# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) / 5 = 1.6

# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input
# test_h = 3
# test_w = 9
# Example Output
# You'll need 6 cans of paint.

import math
def paint_calc(height, width, cover):
    area = width * height
    number_cans = math.ceil(area / cover)

    print (f"You'll need {number_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.

def prime_checker(number):
    count = 0
    for value in range(1, number):
        if (number % value == 0):
            count += 1
    
    if (count == 1):
        print ("It's a prime number.")
    else:
        print ("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)