def del_func():
    try:
        num1 = float(input('Input numerator: '))
        num2 = float(input('Input denominator: '))
    except ValueError:
        return
    if num2 == 0:
        return str('Division by zero is not allowed')
    result = num1 / num2
    return round(result, 2)


division = del_func()
print(division)
