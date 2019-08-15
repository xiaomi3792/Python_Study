# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n * f(n-1)
# print(f(2))

# def f(n):
#     print('\tn =', n)
#     if n == 1:
#         print('Returning...')
#         print('\tn =',n,'return:',1)
#         return 1
#     else:
#         r = n * f(n-1)
#         print('\tn =',n,'return:',r)
#         return r
# print('Call f(5)...')
# print('Get out of f(n),and f(5) =',f(5))

# def a_monk_telling_story():
#     print('山上有座庙，庙里有个和尚，和尚讲故事，他说…… ')
#     return a_monk_telling_story()
#
# print(a_monk_telling_story())

# def teach_youself(anything):
#     while not create():
#         learn()
#         practice()
#     return teach_youself(another)
#
# print(teach_youself(coding))

def teach_yourself(anything):
    while not create():
        learn()
        practice()
    return teach_yourself(another)

print(teach_yourself(coding))