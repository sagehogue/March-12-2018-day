# # lst = []
# #
# # for i in range(10):
# #     lst.append(i)
# #
# # print(lst)
# # lst_comp = [i for i in range(10)]
# # print(lst_comp)
# string = '4556 7375 8689 9855'
# lst = [int(i) if i.isdigit() else '' for i in string]
# lst = [int(i) for i in string if i.isdigit()]
# # for i in string:
# #     lst.append(int(i))
# # print(lst)
#
#
# print(lst)
# tup = (i for i in range(10))
#
# running = True
#
# while running:
#     try:
#         print(tup.__next__())
#     except StopIteration:
#         running = False
# else:
#     print('No more things to print!')
from blackjack.card import Card
rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
SUIT = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

d = [Card(R, S, V) for S in SUIT for R, V in {key:value for key, value in zip(rank, value)}.items()]
print(d)
