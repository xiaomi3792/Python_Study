# def say_hi(*names):
#     for name in names:
#         print(f'Hi, {name}!')
#
# names = ('mike', 'john', 'zeo')
# print(say_hi(*names))
# #print(say_hi())
# #print(say_hi('ann'))
# #print(say_hi('mike','john','zeo'))

def say_hi(greeting,*names,capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting},{name}!')
#say_hi('Hello','mike','john','zeo')
say_hi('Hello','mike','john','zeo',capitalized=True#)
