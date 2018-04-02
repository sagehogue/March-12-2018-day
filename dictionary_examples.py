# # # dict()
# # # dictionary = {1.1: 'value1', 'key2': 'value2'}
# #
# # # print(dictionary['key'])
# phonebook = {
#     'jones': {'first_name': 'Chris', 'last_name': 'Jones', 'phone': '503277910'}
# }
# phonebook2 = {'dover': {'first_name': 'Sheri', 'last_name': 'Dover', 'phone': '5552112123'}}
# # print(phonebook)
# # # # print(phonebook['jones'])
# # # # print(phonebook['jones']['first_name'])
# # name_to_add = 'jones'
# # while name_to_add in phonebook: # False
# #     print('Name is {}'.format(name_to_add))
# #     print('Name exists, adding _x to end...')
# #     name_to_add += "_x") # jones_x
# #
# # phonebook[name_to_add] = {'first_name': 'Sheri', 'last_name': 'Dover', 'phone': '5552112123'}
# # print(phonebook)
# # # print('Deleting')
# # # del phonebook['dover']
# # # print(phonebook)
# #
# # tup = ('wdf', 'asg', ['asdf', 'asdf', 'rew'])
# # tup[-1].append('123')
# # print(tup)
# # try:
# #     print(phonebook['jones'])
# # except KeyError:
# #     print('There is no key by that value!')
# # except ValueError:
# #     print('DOONT DO THAT!')
# # finally:
# #     print('GO!')
# phonebook.update(phonebook2)
#
# # print(phonebook)
# print(list(phonebook.keys()))
# print(list(phonebook.values()))

phonebook = {'key1': 'value1', 'key2': 'value2'}

# print(list(phonebook.items()))
newvar = phonebook.get('key11')

print(newvar)
