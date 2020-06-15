# /usr/bin/env python
# -*- coding: UTF-8 -*-
"""this a test class module"""
from basic import test_class


def sort(a, b, c):
    int_list = []
    if a > b:
        if a > c:
            if b > c:
                int_list = [a, b, c]
            else:
                int_list = [a, c, b]
        else:
            int_list = [c, a, b]
    else:
        if a < c:
            if b < c:
                int_list = [c, b, a]
            else:
                int_list = [b, c, a]
        else:
            int_list = [c, a, b]
    return int_list


if __name__ == '__main__':
    a = input("input first num:")
    b = input("input second num:")
    c = input("input third num:")
    sort_list = sort(a, b, c)
    print(sort_list)
    sort_list.reverse()
    print(sort_list)
    foo = test_class.FooClass("aa")
    print(foo.addMe2Me(4))
