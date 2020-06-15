from basic import christmastree
from basic.christmastree import fun_christmastree  # 也可以引入该函数

if __name__ == '__main__':
    print(christmastree.pinetree)  # christmastree表示一个模块 引入
    fun_christmastree()
    help('modules')