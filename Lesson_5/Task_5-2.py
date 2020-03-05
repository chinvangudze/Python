f_2 = open('file_5-2.txt', 'r+')
line_qty = 0
try:
    for el in f_2:
        line_qty = line_qty + 1
        print(f'String No.{line_qty}: {el}')
except IOError:
    print('Произошла ошибка ввода-вывода!')
finally:
    f_2.close()

f_2 = [len([len(i) for i in x.rstrip().split()]) for x in open("file_5-2.txt", "r+") if x.rstrip() != '']
print(f_2)

# Чуть-чуть не хватило времни, чтобы объединить циклы. Выздоровлю, возьму отпуск, нагоню материал:)
