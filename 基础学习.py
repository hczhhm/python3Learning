#!/usr/bin/env python
#-*- coding:utf-8 -*-
#黄致

x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()

counter = 100
miles = 1000.0
name = 'runoob'

print(counter)
print(miles)
print(name)

a = b = c = 12
print(a,b,c,)
a,b,c = 1,3,'nihao'
print(a,b,c,)

print('\n类型：\n')
a,b,c,d = 20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
print(isinstance(b,complex))

print('\n数值运算：\n')
print(5+4)
print(4.3-2)
print(3*7)
print(2/4)
print(2//4)
print(17%3)
print(2**5)

print('\n字符串：\n')
str = 'Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str + 'TEST')


word = 'python'
print(word[0],word[5])
print(word[-1],word[-6])