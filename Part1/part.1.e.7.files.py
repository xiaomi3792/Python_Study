import os
#f = open('D:\\Documents\\GitHub\\Python_Study\\Part1\\test.txt','w')
#将 \  换为 / ，或者 \\，这是因为Python中\t为换行符，而无法识别。

# 删除文件
#print(f.name)
#f.close() # 关闭文件，否则无法删除文件。
# if os.path.exists(f.name):
#     os.remove(f.name)
#     print(f'{f.name} deleted.')
# else:
#     print(f'{f.name} does not exist')

# 读写文件
# f.write('first line\nsecond line\nthird line\n')
# f.close()
# f = open('D:\\Documents\\GitHub\\Python_Study\\Part1\\test.txt','r')

# 读取全部
# s = f.read()
# print(s)
# f.close()

##  文件有很多行的时候，我们可以用 `file.readline()` 操作，这个 Method 每次调用，都会返回文件中的新一行。
# s = f.readline()
# print(s)
# s = f.readline().strip()
# print(s)
# s = f.readline()
# print(s)
# f.close()
#
# for line in f.readlines():
#     print(line)
# f.close()


# a_list = ['first line\n', 'second line\n', 'third line\n','four line\n']
# f = open('D:\\Documents\\GitHub\\Python_Study\\Part1\\test.txt','w')
# f.writelines(a_list)
# f.close()
#
# f = open('D:\\Documents\\GitHub\\Python_Study\\Part1\\test.txt','r')
# for line in f.readlines():
#     print(line)
# f.close()

## with 语句块

# with open('D:\\Documents\\GitHub\\Python_Study\\Part1\\test.txt','w') as f:
#     f.write('first line\nsecond line\nthird line\nfour line\n')
#
# with open('D:\\Documents\\GitHub\\Python_Study\\Part1\\test.txt','r') as f:
#     for line in f.readlines():
#         print(line)
#
# if os.path.exists(f.name):
#     os.remove(f.name)
#     print(f'{f.name} deleted.')
# else:
#     print(f'{f.name} does not exist')

word = 'acenaphthene'
sum = 0
for char in word:
    sum += ord(char) - 96
print(sum)

# def sum_of_word(word):
#     sum = 0
#     for char in word:
#         sum += ord(char) - 96
#     return sum
#
# with open('D:\\Documents\\GitHub\\Python_Study\\Part1\\results.txt','w') as result:
#     with open('D:\\Documents\\GitHub\\Python_Study\\Part1\\words_alpha.txt','r') as f:
#         for word in f.readlines():
#             if sum_of_word(word.strip()) == 100:
#                 result.write(word)
#



# if os.path.exists(f.name):
#     os.remove(f.name)
#     print(f'{f.name} deleted.')
# else:
#     print(f'{f.name} does not exist')