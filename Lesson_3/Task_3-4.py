# 1st variant
def my_func(x, y):
    x = int(input('Enter positive integer: '))
    y = int(input('Enter negative integer: '))
    result = x ** y
    return round(result, 2)


result = my_func(x=1, y=-1)
print(result)


# 2nd variant
def my_func2(x, y):
    x = int(input('Enter positive integer: '))
    y = int(input('Enter negative integer: '))
    if y == -1:
        result = 1 / x
        return result
    i = abs(y)
    while i != 0:
        x2 = x * x
        i = i - 1
    result = 1 / x2
    return result


result = my_func2(x=1, y=-1)
print(result)
