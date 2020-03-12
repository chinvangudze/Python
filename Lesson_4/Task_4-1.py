from sys import argv

# Мария, можете объяснить, пожалуйста, в чем смысл этой фразы? Что за модуль "sys"?

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)

print(float(first_param) * float(second_param) + float(third_param))