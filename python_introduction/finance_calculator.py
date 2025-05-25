
Monthly_income = float(input("Enter your monthly income: "))
Monthly_expenses = float(input("Enter your total monthly expenses: "))
Monthly_savings = Monthly_income - Monthly_expenses
Projected_Savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: {Projected_Savings:.2f} dollars.")

 
 #assuming a 5% interest rate on the savings, the code calculates the projected savings after one year based on the user's monthly income and expenses. The result is printed with two decimal places for clarity.
# This code snippet calculates the projected savings after one year based on user input for monthly income and expenses.²py