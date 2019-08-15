# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"
#
# print(ord('a'))
# print(chr(122))
#
# print(ord('氅')) # 完了，汉字也有你不认识的吧？
# print(chr(25354)) # 这个字估计你也不认识……

# ord('Python') # 这一句会报错


# age = int(input('''Please tell me your age:
#  an int number , e.g: 22
# '''))
# if age < 18:
#     print('I can not sell you drinks...')
# else:
#     print('Have a nice drink!')
#
# s = "He said, it\\'s fine." # raw
# print(s)                   # presentation

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# str.find(sub[, start[, end]])
print('Example of str.find():')
s = """Simple is better than complex.
Complex is better than complicated."""
s.lower().find('mpl')
s.lower().find('mpl', 10)
s.lower().find('mpl', 10, 20) # 没有找到就返回 -1
print()

print('Example of str.rfind():')
# str.rfind(sub[, start[, end]])
# rfind() 返回最后 sub 出现的那次的位置；find()是最早的那次
s.lower().rfind('mpl')
s.lower().rfind('mpl', 10)
s.lower().rfind('mpl', 10, 20) # 没有找到就返回 -1
print()

print('Example of str.index():')
# str.index(sub[, start[, end]])
# 作用与 find() 相同，但如果没找到的话，会触发 ValueError 异常
# https://docs.python.org/3/library/exceptions.html#ValueError
s.lower().index('mpl')
# str.rindex(sub[, start[, end]])
# 作用与 rfind() 相同，但如果没找到的话，会触发 ValueError 异常
s.lower().rindex('mpl')
print()