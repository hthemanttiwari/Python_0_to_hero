# My Day 9 learnings Are:

# Python Dictionary - Dictionaries are used to store data values in key:value pairs. 
#                     A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Basic Dictionary 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    123: 456
}

print(programming_dictionary["Bug"])
# Output will be 
# An error in a program that prevents the program from running as expected.
print(programming_dictionary[123])
# Output will be 
# 456

# Overwriting item of dictionary
programming_dictionary[123] = 789

# Adding new item in dictionary
programming_dictionary["Loop"] = "The action of Doing something over and over again."


print(programming_dictionary)
# Output will be 
# {
# 'Bug': 'An error in a program that prevents the program from running as expected.', 
# 'Function': 'A piece of code that you can easily call over and over again.', 
# 123: 789, 
# 'Loop': 'The action of Doing something over and over again.'
# }

#creating emptiy dictoonary
empty_dictionary = {}


# wiping an existing dictonary
#programming_dictionary = {}
#print(programming_dictionary)


# looping throught a dictionary
for key in programming_dictionary:
    print(key)
    # Output Will be
    # Bug
    # Function
    # 123
    # Loop
    print(programming_dictionary[key])
    # Output Will be
    # An error in a program that prevents the program from running as expected.
    # A piece of code that you can easily call over and over again.
    # 789
    # The action of Doing something over and over again.


# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. 
# By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. 
# The final version of the student_grades dictionary will be checked.

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if ((student_scores[key] >= 91) and  (student_scores[key] <= 100)):
        student_grades[key] = "Outstanding"
    elif ((student_scores[key] >= 81) and  (student_scores[key] <= 90)):
        student_grades[key] = "Exceeds Expectations"
    elif ((student_scores[key] >= 71) and  (student_scores[key] <= 80)):
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)


#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists
travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]


# From the below if I have to print "Burger"
'''
{
"order": 
    "starter": 
    {
        1: "Salad", 
        2: "soup"
    }
    "main": 
    {
        1: ["Burger", "Fries"], 
        2: ["steak]
    }
    "dessert": 
    {
        1: ["Ice Cream"], 
        2: ["Cake"]
    }
}

print(order["main"][1][0])

'''


# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.
# You've been to Moscow and Saint Petersburg.

# DO NOT modify the travel_log directly. You need to create a function that modifies it.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_name, no_of_visits, cities_visited):
  travel_log.append({"country": country_name, "visits": no_of_visits, "cities": cities_visited,})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)