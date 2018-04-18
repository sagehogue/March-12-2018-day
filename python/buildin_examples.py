# import random
#
#
fruit = ['apple', 'banana', 'orange', 'grape']
veggies = ['carrot', 'cucumber', 'lettus', 'squash', 'foo', 'bar']
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# reversed_numbers = numbers[::-1]
# # # for i in range(len(fruit)):
# # #     print(i)
# # #     print(fruit[i])
# #
# # # print(list(enumerate(fruit)))
# #
# # # for i in enumerate(fruit):
# # #     print(i)
# # #     # print(type(i[0]))
# # #     # print(type(i[1]))
# # #     foo, bar = i
# # #     print(foo)
# # #     print(bar)
# #
# # for index, value in enumerate(fruit):
# #     print(index)
# #     print(value)
#
# # def fil_func(item):
# #     '''
# #     Returns True if item is an even int.
# #     '''
# #     print(locals())
# #     return item % 2 == 0
#
# # even_numbers = list(filter(fil_func, numbers))
# # even_numbers = list(filter(lambda item: item % 2 == 0, numbers))
# # print(even_numbers)
# # print(globals())
# # help(random)
# # fil_func(100)
#
# mult_numbers = list(map(lambda n, y: (n + y) ** 2, numbers, reversed_numbers))
# print(mult_numbers)

# number = input('enter a number: ')
#
# if number == '1':
#     int_number = 1
# elif number == '2':
#     int_number = 2
# else:
#     int_number = 'NaN'
#
# print(int_number)
# print('I want to run tooO')

print(list(zip(fruit, veggies)))
