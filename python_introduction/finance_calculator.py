monthly_income = int(input('Enter your monthly income: '))
montly_expenses = int(input('Enter your total monthly expenses: '))

monthly_savings = monthly_income - montly_expenses

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))


print('Your monthly savings are $', monthly_savings)
print('Projected savings after one year, with interest, is: $', projected_savings)