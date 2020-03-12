def func_person():
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    age = input('Enter your birth year: ')
    city = input('Enter your city: ')
    email = input('Enter your email: ')
    return f'Hi, {name} {surname}! You was born in {age}, now live in {city}. Your email is {email}'


person = func_person()
print(person)
