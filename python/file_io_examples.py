# with open('text_files\io_text\sample_text.txt', 'r') as f:
#     text = f.read()
#
# print all text in file
# print(text)
#
# with open('text_files\io_text\sample_text.txt', 'r') as f:
#     text_lines = f.readlines()
#
# print(text_lines)
# for i in text_lines:
#     print(i, end='')

with open('text_files/io_text/write_examples.txt', 'w', encoding='utf-8') as f:
    f.write('I love python!\n')


with open('text_files/io_text/write_examples.txt', 'a') as f:
    f.write('I love ruby!\n')
