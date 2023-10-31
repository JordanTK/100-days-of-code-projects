# Tip calculator
amount  = float(input("What was the total bill? $"))
perct_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people split the bill? "))
print(f"Each person should pay: ${round((amount*(100+perct_tip)/100)/people,2)}")