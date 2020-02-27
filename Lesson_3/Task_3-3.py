def my_func():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    num3 = int(input('Enter third number: '))
    num_min = min(num1, num2, num3)
    sum_max2 = num1 + num2 + num3 - num_min
    return sum_max2


sum_max2 = my_func()
print(sum_max2)
