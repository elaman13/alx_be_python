monthly_income = int(input('Enter your monthly income: '))
montly_expenses = int(input('Enter your total monthly expenses: '))

monthly_savings = monthly_income - montly_expenses

annual_interest_rate = 0.05

savings_without_interest = monthly_savings * 12

interest_money = savings_without_interest * annual_interest_rate

projected_savings = savings_without_interest + interest_money

print('Your monthly savings are $', monthly_savings)
print('Projected savings after one year, with interest, is: $', projected_savings)