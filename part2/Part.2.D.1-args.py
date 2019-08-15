# form IPython.core.interactiveshell import Interactiveshell
# Interactiveshell.ast_node_interactivit = "all"

# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword('if'))

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False
    return leap

print(is_leap(2019))

import calendar
print(calendar.isleap(2019))

def increase_one(n):
    n += 1
    return n

n = 1
print(increase_one(n))
print(n)