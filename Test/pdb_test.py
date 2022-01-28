# import sys
#
#
# def func1():
#     for i in range(10):
#         if i%2 ==0:
#             print(i)
#
#         if i%3 ==1:
#             print(f'3的倍数 {i}')
#     ss = {'name':'jack','sex':'man'}
#     for k,v in ss.items():
#         print(k,v)
#
# func1()
#
# class A():
#     def hello(self):
#         return "hahah"
#
# def func2(obj):
#     print("%s被删除" % obj)
#
#
# a = A()
# print(sys.getrefcount(a))
# print(sys.argv)

# import pdb
#
# a = "aaa"
# pdb.set_trace()
# b = "bbb"
# c = "ccc"
# final = a + b + c
# print(final)

import pdb


def f1(s1, s2):  # define subroutine combine, which...
    s3 = s1 + s2   # sandwiches s2 between copies of s1, ...
    return s3  # and returns it.


a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = f1(a, b)
print(final)


# 用法 ：  python -m pdb test.py 非入侵式
# import pdb;pdb.set_trace()    侵入式
