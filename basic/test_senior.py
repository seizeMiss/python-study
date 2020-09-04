# /usr/bin/env python
# -*- coding: UTF-8 -*-
import collections
import json
from functools import reduce, wraps


def multiple(x):
    return x * x


def add(x):
    return x + x


func = [multiple, add]
for i in range(5):
    value = map(lambda x: x(i), func)
    print(list(value))  # 兼容python2和python3

print(2 ** 4)

number_list = range(-5, 5)
filter_val = filter(lambda x: x < 0, number_list)
print(list(filter_val))

product = reduce((lambda x, y: x * y), range(1, 5))
print(product)
print(list(range(1, 5)))

some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'm', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

is_fat = True
state = "fat" if is_fat else "not fat"
print(state)

state = ("skinny", "fat")[is_fat]
print(state)


def hi(name="yasoob"):
    return "hi " + name


print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个
print(greet())
# output: 'hi yasoob'

# 如果我们删掉旧的hi函数，看看会发生什么！
# del hi
print(hi())
# outputs: NameError

print(greet())


# outputs: 'hi yasoob'


def hi(name="yasoob"):  # 函数返回函数
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi()
print(a)
# outputs: <function greet at 0x7f2143c01500>

# 上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
# 现在试试这个

print(a())
# outputs: now you are in the greet() function

a = hi(name='ali')
print(a())
print(hi(name='ali')())


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()
#  outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#  now a_function_requiring_decoration is wrapped by wrapTheFunction()
print(a_function_requiring_decoration.__name__)


# a_function_requiring_decoration()
#  outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()


def logit(func):  # 日志应用
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)
print(result)


#  Output: addition_func was called


#  将日志保存到文件中
def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit()
def myfunc1():
    pass


myfunc1()


# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass


myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串


# 避免对字典的键进行嵌套赋值，出现keyError的错误
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
print(some_dict)
print(json.dumps(some_dict))


# 统计信息
with open('func2.log', 'rb') as f:
    fcount = collections.Counter(f)

print(fcount)

