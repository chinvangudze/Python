revenue = float(input('Please, input your annual revenue in USD: '))
costs = float(input('Please, input your annual costs in USD: '))
profit = revenue - costs
if profit > 0:
    print('You done well this year!')
    profit_margin = profit / revenue
    print(f'Your profit margin is {round(profit_margin, 2)}.')
    employees = int(input('Please, input number of your employees: '))
    profit_employees = profit / employees
    print(f'Your firm profit per employee is ${round(profit_employees, 2)}.')
else:
    print(f'Your losses are ${-profit}! Probably, you need to reconsider your business strategy.')