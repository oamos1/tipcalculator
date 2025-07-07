# Build a calculator 
def calculate_tip(total_bill, tip_percent, people):
    tip_amount = total_bill * (tip_percent / 100)
    total_with_tip = total_bill + tip_amount
    amount_per_person = round(total_with_tip / people)
    return amount_per_person

if __name__ == "__main__":
    print("Welcome to Tip Calculator")
    total_bill = float(input("How much is the total bill? "))
    tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    result = calculate_tip(total_bill, tip_percent, people)
    print(f"Each person should pay: ${result}")
