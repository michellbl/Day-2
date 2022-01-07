# If the bill was $150.00, split between 5 people, with 12% tip
# Each persona should pay (150.00 / 5) * 1.12

def line():
    print("_" * 30)

print("Welcome to the tip calculator")
line()
bill = float(input("What was the total bill? $"))
line()
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
line()
people = int(input("How many people to split the bill? "))
line()
bill_with_tip = ((tip * bill) / 100)
final_bill = (bill_with_tip + bill) / people


print(f"Each person should pay: {round(final_bill,2)}")