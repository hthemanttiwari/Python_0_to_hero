# Program to do calculation
# End result is - https://replit.com/@appbrewery/calculator-final?v=1
# Calculator


# from replit import clear
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    
    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("Pick an operation: ")
        num = float(input("What's the next number?: "))
        
        answer = operations[operation_symbol](num1, num)
        """
        This is same as
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num)
        """
        
        print(f"{num1} {operation_symbol} {num} = {answer}")
        
        value = input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation: ")
        if (value == "y"):
            continue_calculation = True
            num1 = answer
        elif (value == "n"):
            continue_calculation = False
            # clear()
            calculator()
        else:
            print ("Enter valid detail")

# Calling Function
calculator()


"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so: 

https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076

"""