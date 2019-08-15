# def _is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# year_leap_bool = _is_leap
# print(year_leap_bool)
# print(year_leap_bool(800))
#
# print(id(year_leap_bool))
# print(id(_is_leap))
#
# print(type(year_leap_bool))
# print(type(_is_leap))

phonebook = [
    {
        'name': 'john',
        'phone': 9876
    },
    {
        'name': 'mike',
        'phone': 5603
    },
    {
        'name': 'stan',
        'phone': 6898
    },
    {
        'name': 'eric',
        'phone': 7898
    }
]

print(phonebook)
print(list(map(lambda x: x['name'], phonebook)))
print(list(map(lambda x: x['phone'], phonebook)))
