# name = input('What is your name?: ')
# age = input('How old are you?: ')
# birth_year = 2018 - int(age)
# print('Hey, {}!'.format(name))
#
# if birth_year < 1985:
#     if name == 'Chris':
#         print("SOOOOOO  OOOOLLLLLD")
#     else:
#         print('Have a great day Sir or Mam.')
# elif birth_year < 1990:
#     print('Not soo old.')
# else:
#     print('You are super young yo!')
#
# print('You were born in {}'.format(birth_year))

# int()
# float()
# str()

def greeting(name):
    if name[0].lower() == 'c':
        return 'Hello {}'.format(name)
    return 'Hiya {}'.format(name)

print(greeting('Chris'))

print(greeting('Sarah'))
