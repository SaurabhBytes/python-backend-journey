# Salary Calculator


monthly_salary = int(input("Enter Your Monthly Salary :")) 
months_worked = int(input("Number of months worked : "))

total_earnings = monthly_salary * months_worked
annual_salary = monthly_salary * 12
earned_more = total_earnings >= 500000

print("\n---Results---")
print(f"Monthly Salary : {monthly_salary}")
print(f"Months Worked : {months_worked}")
print(f" Total Earnings : {total_earnings}")
print(f" Annual Salary : {annual_salary}")
print(f" Earned More Than 500000: {earned_more}")



