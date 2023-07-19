# My Day 6 learnings Are:

# Functions

# Built-in functions - examples are len(), print(), input(), etc....
# Please visit - https://docs.python.org/3/library/functions.html


# We can reate our own functions.
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


# Reebog World

# 1-Alone State 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# Creating turn Around Function.
# def turn_around():
#     turn_left()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# Draw Square

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_around()

# While Loop

# Syntax is,
# while something_is_true:
    # Do something repeidately

# It is very easy for while loop to go into infinite loop, so mind it.
# example:
# while 5 > 3:
#    print ("Hi")
# This condition will always be true.


# Challange 1:-
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Solution:-

'''
# Creating turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Creating jump function
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Code begins

# We can do this with for loop as well

# for step in range (6):
#     jump()

number_of_hurdels = 6
while (number_of_hurdels > 0):
    jump()
    number_of_hurdels -= 1
    print(number_of_hurdels)

'''

# Chalange 2:-
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# Solution:-

'''

# Creating turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Creating jump function
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Code begins
#for step in range (6):
#    jump()

# while not at_goal():
while not at_goal():
    jump()

'''


# Chalange 3:-
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Solution:-

'''
# Creating turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Creating jump function
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Code begins
#for step in range (6):
#    jump()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

'''


# Chalange 4:-
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Solution:-

'''
# Creating turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Creating jump function
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# Code begins

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

'''


# Chalange 5:-
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Solution:-
'''
# Creating turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Code begins here

# My Solution
while not at_goal():
    if wall_in_front():
        turn_right()
    else:
        move()
        if wall_on_right():
            turn_left()

# Teacher's Solution.     
# Follow along the right edge
# In one of the scenerios, it will go into infinite loop. Revisit on Day 15.
while not at_gail():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

'''

# Please Mind Indentation in Python. 
# Please visit "https://peps.python.org/pep-0008/" to know more about Indentation.
# In python indentation is done by Sapce and Not Tab.