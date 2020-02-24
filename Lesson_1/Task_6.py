result_now = int(input('Please, input your current running distance in km: '))
result_wanted = int(input('Please, input your desired running distance in km: '))
days = 1
while result_now < result_wanted:
    result_now = result_now * 1.1
    # print(round(result_now, 2))
    days = days + 1
print(f'With our training program you will reach this result only in {days} days!')