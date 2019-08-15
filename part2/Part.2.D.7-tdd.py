# def is_leap(year):
#     return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)
#
# print(is_leap(300))

# 根据闰年的定义：
#
# 年份应该是 4 的倍数；
# 年份能被 100 整除但不能被 400 整除的，不是闰年。
# 所以，相当于要在能被 4 整除的年份中，排除那些能被 100 整除却不能被 400 整除的年份。

def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
        if year % 100 == 0:
            if year % 400 !=0:
                r = False
        return r

print(is_leap(4))
print(is_leap(200))
print(is_leap(220))
print(is_leap(400))
print(is_leap(2019))

try:
    f = open('test_file.txt','r')
except FileNotFoundError as fnf_error:
    print(fnf_error)