def html_tag(el):
    def inner(msg):
        return '<{el}>{msg}</{el}>'.format(el=el, msg=msg)

    return inner


paragraph_tag = html_tag('p')
print(paragraph_tag('I like to code on days that end in "y".'))