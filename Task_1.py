variable_1 = 'Hello'
variable_2 = 10
variable_3 = True

print("Hello, stranger! Please, tell me what's your name? ")
user_name = input()
print('Nice to meet you,', user_name, '! How old are you?')
user_age = int(input())
if user_age < 18:
    print('Oh, you are too young! Access denied.')
elif 18 < user_age < 35:
    print('Good to know, friend! Come on, go ahead!')
elif user_age > 36:
    print('Sorry to hear... Have you already chosen a place in cemetery? Go further anyway.')