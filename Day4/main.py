# My Day 4 learnings Are:

# What is Modules?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.


# Random Modules.

# To importe the random modules.
import random

# For int
random_integer = random.randint(1, 10)
print (random_integer)
# Output will be any random no. between 1 and 10.

# For float
random_float = random.random()
print (random_float)
# Output will be any random float nos. between 0 and 1. 
# random.random() will print random float nos. only between 0 and 1. 

# To get a random number between 0 to 5, we can simply multiply the random no. 5.
random_float = random.random() * 5
print (random_float)

# Please visit "https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences" to know about different random functions.



# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. 
# Then use that number to print out Heads or Tails.
# e.g. 1 means Heads 0 means Tails
#Remember to use the random module

import random

random_number = random.randint(0, 1)

if (random_number == 1):
    print("Heads")
else:
    print("Tails")


# Python Lists (DataStructures).
# We can have list with mixed dattypes as well.

fruits = ["Apple", "Orange", "Mango", "Cherry"]

# In Lists counting starts with 0.
print (fruits[0])
# Output will be Apple
print (fruits[2])
# Output will be Mango

# If Negative no is mentioned than counting stats from last.
print (fruits[-1])
# Output will be Cherry
print (fruits[-2])
# Output will be Mango

# Playing with Lists (Adding/Removing values in a list). 

# We can change the values as well.
fruits[1] = "Orange Fruit"
print (fruits)
# Output will be 
# ["Apple", "Orange Fruit", "Mango", "Cherry"]

# We can add new values as well.
fruits.append("Guava")
print (fruits)
# Output will be 
# ["Apple", "Orange Fruit", "Mango", "Cherry", "Guava"]

# List index out of range error and length of lists.
lenght_fruits = len(fruits) 
# print (fruits[lenght_fruits])
# length is from 1 but list count starts from 0 so use lenght - 1
print (fruits[lenght_fruits - 1])
# Output will be Guava

# Please visit "https://docs.python.org/3/tutorial/datastructures.html" to know more about list functions.


# Nested Lists.

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits1 = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegitables1 = ["Spinach", "Kale", "Pears", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits1, vegitables1]

print (dirty_dozen)
# Output will be 
# [["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"], ["Spinach", "Kale", "Pears", "Tomatoes", "Celery", "Potatoes"]]

# Here dirty_dozen has fruits1 at "0th position" and vegitables1 at "1th position".
# So lets say we want to print the 4th value in the fruits1 list.
# We will have.
print (dirty_dozen[0][4])
# Output will be Peaches

# Here 1st [] represent list no. and 2nd [] represent the value in list number.
# Simmilarly for from vegitables1 list I want the output to be Tomatoes.
# So, I will have to print
print (dirty_dozen[1][3])


# String to list Conversion. By using split() function.
# Please visit "https://www.askpython.com/python/string/convert-string-to-list-in-python" to know more about String to list Conversion.


# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. 
# For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
# Example Output
# Michael is going to buy the meal today!

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list_length = len(names)
random_number = random.randint(0, (list_length - 1))

print (names[random_number] + " is going to buy the meal today!")

# with random choice function
# random_choice = random.choice(names)
# print (random_choice + " is going to buy the meal today!")