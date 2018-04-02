with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

name = 'chris'
start_sym = '{{'
end_sym = '}}'
replace = content[content.find(start_sym): content.find(end_sym) + 2]
first_half = content[:content.find(start_sym)]

second_half = content[content.find(end_sym)+2:]
# print(second_half)
total = '{} {} {}'.format(first_half, name, second_half)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(total)
