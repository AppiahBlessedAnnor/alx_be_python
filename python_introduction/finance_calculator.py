# Get user input to project his annual earnings

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

# Used string concatenation to remove space between '$' and money
print ("Your monthly savings are", "$" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is:", "$" + str(int(projected_savings)) + ".")