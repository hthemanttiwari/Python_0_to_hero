# My Day 10 learnings Are:

# Functions with outputs
def format_name(f_name, l_name):

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


camel_case_name = format_name("HEmaNt", "tIWarI")
print (camel_case_name)

#the above can be replaced with
print(format_name("HEmaNt", "tIWarI"))


def format_name(f_name, l_name):
    """
    Docstring: Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods.
    It’s specified in source code that is used, like a comment, to document a specific segment of code. 
    Unlike conventional source code comments, the docstring should describe what the function does, not how.
    
    """
    if f_name == "" or l_name == "":
        # return
        # This will return none.
        return "You did not provide valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

camel_case_name = format_name("HEmaNt", "tIWarI")
print (camel_case_name)

#the above can be replaced with
print(format_name(input("What is your 1st Name?: "), input("What is your last Name?: ")))


# In the starting code, you'll find the solution from the Leap Year challenge. 
# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
# it should return True if it is a leap year and return False if it is not a leap year.
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

def is_leap(year):
    if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_days[month-1] == 28:
        if is_leap(year) == True:
            return 29
        else:
            return 28
    else:
        return month_days[month-1]
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Nexting Function: A nested function is a function that is completely contained within a parent function.
# We can have nesting function as
def nesting_function():
    # Do this
    # Then this
    # Nexting the function
    nesting_function()

# Calling function
nesting_function()
