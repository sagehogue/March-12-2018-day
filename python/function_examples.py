# def greeting():
#     print('Hello Chris!')
#
# greeting()
# name = input('What is your name?: ')
#
# def get_question(question):
#     return input('{}?: '.format(question))
#
# name = get_question('What is your username')
# print(name)
# age = get_question('How old are you')
# print(age)
#
# def greeting():
#     name = 'YOU GET NO NAME!!!'
#     return name
#
# def somenewfunc():
#     print(name)
#     thing = 'something'
# new_name = greeting().lower()
# print(new_name)
# print('Hello {}!'.format(name))
import random
options = [
    "It is certain", "It is decidedly so", "Without a doubt",
    "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely",
    "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
    "Ask again later", "Better not tell you now", "Cannot predict now",
    "Concentrate and ask again", "Don't count on it", "My reply is no",
    "My sources say no", "Outlook not so good",
    ]


# 1. Print a welcome screen to the user.
def welcome():
    return 'Welcome! You can ask questions!'


# 3. Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
def ask_question():
    return input('What is your queston for the MAAAAGIC 8 BALLLL?: ')


# 5. Display the result of the 8-ball.
def display_results(question, answer):
    return 'You asked: {}\nMy answer: {}'.format(question, answer)


def magic_8ball():
    q = ask_question()
    a = random.choice(options)
    print(display_results(q, a))


print(welcome())
magic_8ball()
while True:
    q = input('Do you wish to play again?(y/n): ').lower() or 'None'
    if q in 'yes':
        magic_8ball()
    elif q in 'no':
        exit()
    else:
        print('I did not understand that...')
