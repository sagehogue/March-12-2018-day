# string = 'I am a string!'
# integer = 3
# # list()
# lst = [string, integer, 4, 'the', [1, 2, 3.14]]
#
# print(lst[4], lst[4][1])
# print(lst[1:3])
#
# number = list(range(1, 101))
# print(number[10000000])
# numbers = list(range(40))
# # print(numbers)
# # print(41 in numbers)
# numbers_2 = numbers[::]
# # print(numbers)
# numbers[0] = 40
#
# print(numbers)
# print()
# print(numbers_2)

fruit = ['apple', 'banana', 'banana']

# fruit.append('grape')
#
# fruit.insert(0, 'orange')
# print(fruit)
#
# # for i in range(fruit.count('banana')):
# #     fruit.remove('banana')
# print(fruit)
#
# fruit.pop()
# print('You removed {}.'.format(removed_item))
# print(fruit)
more_fruit = ['orange', 'grape']
total = fruit + more_fruit
# fruit.extend(more_fruit)
# fruit.append(more_fruit)
# print(fruit + more_fruit)
#
# print(fruit.index('banana'))
# fruit.reverse()
# reversed_fruit = fruit[::-1]
total.sort()
print(total)
