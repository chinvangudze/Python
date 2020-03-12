f_1 = open('file_5-1.txt', 'w+')
line = str('text')
try:
    with open('file_5-1.txt', 'a+') as f_1:
        while line != ' ':
            line = str(input('Введите строку: '))
            f_1.write(line)
            f_1.write('\n')
except IOError:
    print('Произошла ошибка ввода-вывода!')
