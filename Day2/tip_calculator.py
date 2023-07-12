# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Code is Below

print ("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

percentage = int(input("What percentage tip would you like to give? "))
tip_percentage = (1 + (percentage / 100))

number_people = int(input("How many people will split the bill? "))

total_bill = ((bill / number_people) * percentage)

# final_result = "{:.2f}".format(total_bill)

# Method 1
final_result = round(total_bill, 2)
# Method 2
final_amount = "{:.2f}".format(final_result)

print (f"Each person should pay: ${final_amount}")