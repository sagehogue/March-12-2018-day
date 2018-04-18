# import random
#
# user_guess_count = 0
# computer_guess = random.randrange(1, 11)
#
# while True:
#     user_guess = int(input('What number do you guess?: '))
#     user_guess_count = user_guess_count + 1
#     if user_guess > computer_guess:
#         print('You guessed too high!')
#     elif user_guess < computer_guess:
#         print('You guessed too low!')
#     else:
#         print('YOU GUESSED IT!! YAY!!! you guessed it in {}'.format(user_guess_count))
#         break

# Tell the user whether their current guess is closer than their last.
# This can be done by maintaining a variable containing the last guess outside
# the loop, then comparing the last guess to the current guess, and check if
# it’s closer. Hint: you’re interested in comparing the two absolute
# differences: abs(current_guess-target) and abs(last_guess-target).
# import random
#
# user_guess_count = 0
# computer_guess = random.randint(1, 100)
# user_last_guess = 0
#
#
# while True:
#     user_guess = int(input('What number do you guess?: '))
#     user_guess_count = user_guess_count + 1
#
#     if user_guess > computer_guess:
#         print('You guessed too high!')
#     elif user_guess < computer_guess:
#         print('You guessed too low!')
#     else:
#         print('YOU GUESSED IT!! YAY!!! you guessed it in {}'.format(user_guess_count))
#         break
#
#     if abs(user_guess - computer_guess) < abs(user_last_guess - computer_guess):
#         print('You\'re getting warmer!')
#     else:
#         print('You\'re getting colder!')
#     user_last_guess = user_guess

# import random
#
# computer_guess_count = 0
# computer_guess = random.randint(1, 100)
# computer_last_guess = 0
# computer_high_guess = 100
# computer_low_guess = 1
# first_run = True
# user_number = int(input('What number do you pick in rage of 100?: '))
# while True:
#     computer_guess_count += 1
#     print(computer_guess)
#     query = input('Is the computers guess lower or higher or correct?: ').lower()
#     if query == 'lower':
#         computer_low_guess = computer_guess
#         computer_guess = ((computer_high_guess + computer_low_guess) // 2)
#     elif query == 'higher':
#         computer_high_guess = computer_guess
#         computer_guess = ((computer_high_guess + computer_low_guess) // 2)
#     elif query == 'correct':
#         print('Yes I am a computer. I am always correct. It only took me {} trys.'.format(computer_guess_count))
#         break
#     else:
#         print("I don't understand...")
