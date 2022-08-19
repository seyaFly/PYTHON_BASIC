# -*- coding: utf-8 -*-

#---int类型显示转换----

print("\n*******Int类型转换******\n")

print(int(1))     #  输出结果为 1
print(int(2.8))   #  输出结果为 2
print(int("3"))   #  输出结果为 3

print("\n*******flot类型转换******\n")
print(float(1))     #  输出结果为 1.0
print(float(2.8))   #  输出结果为 2.8
print(float("3"))   #  输出结果为 3.0
print(float('14.2'))   #  输出结果为 14.2

print("\n*******Str类型转换******\n")
print(str(1))       #  输出结果为 '1'
print(str(2.8))     #  输出结果为 '2.8'
print(str("seya"))  #  输出结果为 'seya'


#隐式类型转换
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print("datatype of num_int:",type(num_int))  # int类型
print("datatype of num_flo:",type(num_flo))  # float类型
print("Value of num_new:",num_new)           # 结果为 124.23
print("datatype of num_new:",type(num_new))  # flow类型