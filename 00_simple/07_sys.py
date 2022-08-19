# coding=utf-8

import sys
try:
    # 输入整型值
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)
    # 异常处理
except ValueError:
    print('请输入正确的整型值')
