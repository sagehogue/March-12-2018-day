# def make_p_tag(text):
#     return '<p>{}</p>'.format(text)
#
#
# def make_div_tag(text):
#     return '<div>{}</div>'.format(text)


# print(make_p_tag('I like to code.'))
# print(make_div_tag('Some words!'))

# def html_tag_factory(el):
#     def inner(text):
#         return '<{}>{}</{}>'.format(el, text, el)
#     return inner


# p_tag = html_tag_factory('p')
# div_tag = html_tag_factory('div')

# print(div_tag('I like to code!'))
def html_decorator(el):
    def deca(f):
        def wrapper(*args, **qwargs):
            return '<{}>{}</{}>'.format(el, args[0], el)
        return wrapper
    return deca


@html_decorator('p')
def text(t):
    return t


print(text('hi'))

# def our_decorator(func):
#     def inner(text):
#         print('Befoire calling {}'.format(func.__name__))
#         print(func(text))
#         print('After calling {}'.format(func.__name__))
#     return inner
#
#

#
#
# @our_decorator
# def foo(t):
#     return t
#
#
# text('I like to code!')
# foo('This is more text to test')