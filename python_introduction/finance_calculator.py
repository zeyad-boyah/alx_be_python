monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
# Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05) annual interest rate of 5%
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
