# greeting = 'Hello, {}!'
# name = input('What is your name?: ')
# total_greeting = greeting.format(name.capitalize())
#
# print(total_greeting)
# print(total_greeting.count('l'))
# print(greeting.index('y'))

# print('Chris' * 5)
# words = "The-quick-brown-fox-jumped-over-the-lazy-dog."
words = "The quick brown fox jumped over the lazy dog."
print(words)
print()

word_list = words.split()
print(word_list)
print()

words_dash_case = '-'.join(word_list)
print(words_dash_case.lower())
