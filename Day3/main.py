# My Day 1 learnings Are:

#greater than and less than operations.

# > Greater-than
# < Less-than
# >= Greater-than equal to
# <= Less-than equal to
# == Equal to
# != Not Equal to


# if/else condition.
# Syntax example is

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print ("You can ride the rollercoster!")
else:
  print ("You can not ride the rollercoster!")


# Nested if condition.
# Syntax example is
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))

if height >= 120:
  print ("You can ride the rollercoster!")
  if (age <= 18):
    print ("Please pay $7.")
  else:
    print ("Please pay $12.")
else:
  print ("You can not ride the rollercoster!")


# elif condition.
# Syntax example is
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))
if (height >= 120):
  print ("You can ride the rollercoster!")
  if (age < 12):
    print ("Please pay $5.")
  elif (age <= 18):
    print ("Please pay $7.")
  else:
    print ("Please pay $12.")
else:
  print ("You can not ride the rollercoster!")


# Multiple if Conditions.
# Syntax example is
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))
bill = 0
if (height >= 120):
  print ("You can ride the rollercoster!")
  if (age < 12):
    bill = 5
    print ("child Tickets are $5.")
  elif (age <= 18):
    bill = 7
    print ("Youth Tickets are $7.")
  else:
    bill = 12
    print ("Adult tickets are $12.")

  wants_photos = input ("Do you want photos taken? Y or N.")
  if (wants_photos == "Y"):
    #Add $3 to their bill.
    bill += 3
  print (f"Your final bill is ${bill}")
else:
  print ("You can not ride the rollercoster!")



# The modulo [percentage sign (%)] for finding the rmainder.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.




# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder. 
# e.g. 86 is even because 86 ÷ 2 = 43 
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

number = int(input("Which number do you want to check? "))

if (number % 2 == 0):
    print ("This is an even number.")
else:
    print ("This is an odd number.")


# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# Warning you should round the result to the nearest whole number. 
# The interpretation message needs to include the words in bold from the interpretations above. 
# e.g. underweight, normal weight, overweight, obese, clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round((weight / height ** 2))

if (bmi < 18.5):
    print (f"Your BMI is {bmi}, you are underweight.")
elif (bmi < 25):
    print (f"Your BMI is {bmi}, you have a normal weight.")
elif (bmi < 30):
    print (f"Your BMI is {bmi}, you are slightly overweight.")
elif (bmi < 35):
    print (f"Your BMI is {bmi}, you are obese.")
else:
    print (f"Your BMI is {bmi}, you are clinically obese.")


# Logical operators - and, or, not operators.
# A and B
# C or D
# not E

# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE

# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400
# e.g. The year 2000: 
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)


year = int(input("Which year do you want to check? "))

if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
    print ("Leap year.")
else:
    print ("Not leap year.")


# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0

if (size == "S"):
    price = 15
elif (size == "M"):
    price = 20
else:
    price = 25

if (add_pepperoni == "Y"):
    if (size == "S"):
        price += 2
    else:
        price += 3
if (extra_cheese == "Y"):
    price += 1

print (f"Your final bill is: ${price}.")


# count() functions.
sentence = 'Mary had a little lamb'
print (sentence.count('a'))
# Output will be 4

print ('Mary had a little lamb'.count('a'))
# Output will be 4

# lower() functions.
sentence = 'Mary had a little lamb'
print (sentence.lower())
# Output will be  - mary had a little lamb

print ('Mary had a little lamb'.lower())
# Output will be  - mary had a little lamb


# ff a = 10
# a = a + 20 is same as a += 20
# Same goes for all mathemetical operations.
# For usage, please check the true_love_calculator.py file.



# Ignoring symbol using \ in a String.
# Multiline String using 3 single quots ('''  ''')
# For usage of Both Please check the game.py file.


# For Fun ASCII Arat please visit "https://ascii.co.uk/art".