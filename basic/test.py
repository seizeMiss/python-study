# -*- coding: UTF-8 -*-
import sys
import math
import traceback


def get_name(param):
    for a in param:
        if a == 'a':
            print('hello ' + a)
        else:
            print('error ' + a)
    param = '123'
    return param


def greet_me(**kwargs):
    for key, val in kwargs.items():
        print("{0} == {1}" . format(key, val))


if __name__ == '__main__':
    str1 = "hello"
    str1 += " aa"
    print(str1[0:7])  # 字符串
    print('hello')
    list1 = ["test", "hello", 12]  # 集合
    print(list1[0])
    tuple1 = (1, '2a', 3, list1)  # 元组 不可变
    list1 = list1 + [34]
    print("list1:", )
    print(list1)
    # tuple1.__add__('55',)
    print(tuple1[0:2])
    for index, value in enumerate(tuple1):  # 既可以获得值也可以获得下标
        print(index),
        print(value)
    dict1 = {"name": "aa", "age": 23}  # 字典 类似 Map
    print(dict1["name"])
    print(dict1.keys())
    print('name:' + dict1['name'] + ',age:' + str(dict1['age']))
    print(range(1, 5, 2))  # 获得 1-5（不包括5）的值，步长是2
    print(get_name('abc'))
    # name = raw_input('please input your name')  # 用户输入 str 值
    # age = input('please input your age') # 用户输入 int 值
    # print(type(name))
    # print type(age)

    print("%s is a %d language" % ('python', 22))
    # print >> sys.stderr, 'print error'
    # help(raw_input())
    print(8.0 / 6)  # / 传统除法
    print(8 // 6)  # // 底板除
    index = int(4)
    if 5 > index > 2:  # 和 and 或 or
        print(index)
    # 不支持 自增和自减
    # 支持复数

    bigInt = 1111111111111111111111111111111111
    print(type(bigInt))

    sqdEvent = [x ** 2 for x in range(7) if x // 2]  # 列表的解析
    for a in sqdEvent:
        print(a)

    print(sys.version)

    try:
        a = 1 / 0
    except Exception as e:
        print(e)
        print(str(e))
        print(repr(e))
        # print "print:" + traceback.print_exc()
        print(traceback.format_exc())

    try:
        a = 1 / 0
    except Exception as e:
        print(traceback.format_exc())
        print("aa")

    # lambda表达式
    r = 10
    result = lambda radius: math.pi * radius * radius
    print("半径为r", r, '的圆的面积是：', result(r))
    print(result)

    greet_me(name='lance', age='25')
