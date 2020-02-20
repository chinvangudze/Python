time = int(input('Enter quantity of seconds: '))
s = time % 60
m = time % 3600 // 60
h = time // 3600

if len(str(s)) == 1:
    s = f'0{s}'
if len(str(m)) == 1:
    m = f'0{m}'
if len(str(h)) == 1:
    h = f'0{h}'

print(f'Exact time is {h}:{m}:{s}')
