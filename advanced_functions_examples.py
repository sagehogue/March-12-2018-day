# def greeting(name, age=0):
#     return 'Hello {}. You are {} years old.'.format(name, age)
#
# print(greeting('Chris', 22))
#
# def add_numbers(*args):
    # print(args[100])
    # total = 0
    # for i in args:
    #     if isinstance(i, int):
    #         total += i
    #     else:
    #         raise ValueError('Must be int')
    # return args#total
#
# a = 100
# print(add_numbers(1,'a',2,3,4,5,6,7,8))
def contacts(work_name,*args, **kwargs):
    if 'name' in kwargs:
        print(kwargs['name'])
    print(args)
    print(kwargs)


contacts('a', 'b', a=35, name='chris', phone=5032779710)
contacts('a', age=35, phone=5032779710)
