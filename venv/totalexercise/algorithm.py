#sqrt_newton
# import math
# from math import sqrt
# num=float(input("请输入数字："))
# def sqrt_newton(num):
#     x=sqrt(num)
#     y=num/2.0
#     count=1
#     while abs(y-x)>0.0000001:
#         print(count,y)
#         count+=1
#         y=((y*1.0)+(1.0*num)/y)/2.000
#     return y
# print(sqrt_newton(num))
# print(sqrt(num))

from math import  sqrt
num=float(input("请输入数字："))
def sqrt_num(num):
    y=num/2
    count=1
    x=sqrt(num)
    while abs(x-y)>\
            0.000001:
        print(count,y)
        y=(y+num/y)/2
        count+=1
    return y
print(sqrt_num(num))
print(sqrt(num))
