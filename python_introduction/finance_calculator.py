monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

monthly_savings = monthly_income - monthly_expenses

annual_interest_rate = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * annual_interest_rate * 12)

print('Your monthly savings are $', monthly_savings)
print('Projected savings after one year, with interest, is: $', projected_savings)