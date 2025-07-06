# Build a calculator 

print ( " Welcome to Tip Calculator")

total_bill= float(input("How much is the total bill"))

tip_percent = int(input("How much tip would you like to give? 10, 12, or 15 "))

people = int(input("How many people to split the bill ")
)

# Calculate the total bill divided by bill amount over 100 to get percentage
tip_amount = total_bill * (tip_percent / 100)
total_with_tip = total_bill + tip_amount

# Get the total Bill with per person 
amount_per_person =  round(total_with_tip / people
)
# this should print the total amount
print(f"each person should pay: ${amount_per_person}")