# -*- coding: utf-8 -*-

#打印关键字
import keyword
print ("\n**********************************关键字*****************************************************************************\n")
print(keyword.kwlist)

#基本数据类型
print ("\n**********************************基本数据类型******************************************************************************\n")
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
friends = ["bob", "jim", "jimmy"] #列表
car = {"wheel" : 4,"seat": 4} #字典
vitual = 3 + 4j  #Complext
bBool = True  #布尔值
tupleType = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
setType = { 'abcd', 786 , 2.23, 'runoob', 70.2  }

print(isinstance(counter, int) )
print(isinstance(miles, float) )
print(isinstance(name, str) )
print(isinstance(friends, list) )
print(isinstance(car, dict) )
print(isinstance(vitual, complex) )
print(isinstance(bBool, bool) )
print(isinstance(tupleType, tuple) )
print(isinstance(setType, set) )


del counter, miles, name, friends, car, vitual, bBool #删除变量

print ("\n**********************************赋值方式1******************************************************************************\n")
#赋值方式1
fooA = fooB = fooC = 1;
print("fooA = " + str(fooA))
print("fooB = " + str(fooB))
print("fooC = " + str(fooC))

del fooA,fooB,fooC #删除变量
print ("\n**********************************赋值方式2******************************************************************************\n")
#赋值方式2
tooA, tooB, tooC = 1, 2, 3; 
print("tooA = " + str(tooA))
print("tooB = " + str(tooB))
print("tooC = " + str(tooC))


del tooA,tooB,tooC #删除变量
print ("\n**********************************数值运算******************************************************************************\n")

print(5 + 2);  # 结果为7
print(5 - 2);  # 结果为3
print(5 * 2);  # 结果为 10
print(5 ** 2); # 结果为 5的平方 25
print(5 / 2);  # 结果为 2.5
print(5 // 2); # 结果取整数 2
print(5 % 2); # 结果取余数 3

print ("\n**********************************String 运算******************************************************************************\n")

strSeya = 'Seyafool'

print (strSeya)          # 输出字符串
print (strSeya[3])       # 输出从左到右第4个字符串，需要从0开始， 0，1，2，3
print (strSeya[-4])      # 输出从右到左第4个字符串，序号从-1开始， -1， -2， -3
print (strSeya[0:-1])    # 输出第一个到倒数第二个的所有字符
print (strSeya[0])       # 输出字符串第一个字符
print (strSeya[2:5])     # 输出从第三个开始到第五个的字符
print (strSeya[2:])      # 输出从第三个开始的后的所有字符
print (strSeya * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (strSeya + "TEST") # 连接字符串()

print ("Seya\nfool")     # 使用转义字符换行
print (r"Seya\nfool")    # 使用 r 使转义字符无效，正常输出

del strSeya

print ("\n**********************************List******************************************************************************\n")

#列表数据可更改

leftlist = [ 'abcd', 786 , 2.23, 'seya', 70.2 ]
rightlist = [123, 'seya']

print (leftlist)            # 输出完整列表
print (leftlist[0])         # 输出列表第一个元素
print (leftlist[1:3])       # 从第二个开始输出到第三个元素
print (leftlist[2:])        # 输出从第三个元素开始的所有元素
print (rightlist * 2)    # 输出两次列表
print (leftlist + rightlist) # 连接列表

del leftlist,rightlist

print ("\n**********************************tuple******************************************************************************\n")

#元组数据不可更改
leftTuple = ( 'abcd', 786 , 2.23, 'seya', 70.2 )
righTuple = (123, 'seya')

print (leftTuple)            # 输出完整元组
print (leftTuple[0])         # 输出列表第一个元素
print (leftTuple[1:3])       # 从第二个开始输出到第三个元素
print (leftTuple[2:])        # 输出从第三个元素开始的所有元素
print (leftTuple * 2)        # 输出两次列表
print (leftTuple + righTuple) # 连接列表

del leftTuple, righTuple

print ("\n**********************************集合******************************************************************************\n")

sites = {'Google', 'Taobao', 'seya', 'Facebook', 'Zhihu', 'Baidu', 'Facebook'}
print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'seya' in sites :
    print('seya 在集合中')
else :
    print('seya 不在集合中')


# set可以进行集合运算
setA = set('abracadabra')
setA.add(100)
setB = set('alacazam')

print(setA)
print(setA - setB)     # setA 和 setB 的差集
print(setA | setB)     # setA 和 setB 的并集
print(setA & setB)     # setA 和 setB 的交集
print(setA ^ setB)     # setA 和 setB 中不同时存在的元素

del setA, setB