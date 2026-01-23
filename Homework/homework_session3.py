monthly_income = int(input("Enter monthly income :"))
monthly_expenses = int(input("Enter monthly expenses :"))
dependents = int(input("Number of dependents : "))

savings = monthly_income - monthly_expenses
print(f"\nMonthly Savings")

if savings >= 10000: 
    print("Excellent Savings")

elif savings >=5000:
    print("Good Savings")    

elif savings >=0:
    print("Okay, but save more")      

else:
    print("You're spending more than you earn")


if dependents > 0:
    print(f"You have {dependents} dependents, manage wisely")    
