# -*- coding: UTF-8 -*-


class FooClass(object):
    version = 0.1  # class (data) static attribute
    __name = 'FooClass'

    # title = 'FooClass title'

    def __init__(self, nm='John Doe', title='FooClass title'):  # 创建完成class就执行
        self.name = nm  # class instance (data) attribute
        print('Created a class instance for', nm)
        self.__title = title  # title只读

    @property
    def title(self):
        return self.__title

    def get_name(self):
        return self.__name

    def show_name(self):
        print('Your name is', self.name)
        print('My name is', self.__class__.__name__)

    def show_version(self):
        print(self.version)  # references FooClass.version

    def addMe2Me(self, x):  # does not use 'self'
        return x + x


class Swan:
    """天鹅类"""
    __neck_swan = '天鹅的脖子很长'

    def __init__(self):
        print('__init__', Swan.__neck_swan)


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    foo = FooClass('lance')
    # foo.title = 'lance title' # 设置保护属性，无法修改值，只能只读
    print(foo.title)

    # foo.__init__('lance')
    print(foo.show_name())
    foo2 = FooClass()
    FooClass.version = 0.2
    FooClass.__name__ = 'dragon'
    foo2.show_version()
    foo2.show_name()
    foo3 = FooClass()
    foo3.show_version()
    foo3.show_name()
    # print dir(foo)  #查看对象的属性
    print(foo.get_name())

    swan = Swan()
    print('加入类名', swan._Swan__neck_swan)  # 通过 类的实例名._类名__xxx  访问
    # print('直接访问', swan.__neck_swan) # 不能直接访问

    rect = Rect(10, 20)
    print(rect.area)
