print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

print(f"Each person should pay: "
      f"{round((bill_amount + (bill_amount * tip) / 100) / people,2)}")
