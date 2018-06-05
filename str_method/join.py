#-*-  coding=utf-8 -*-
print(help(str.join))
'''
join(...)
    S.join(iterable) -> string
    
    Return a string which is the concatenation of the strings in the
    iterable.  The separator between elements is S.

None
join方法是将字符串用指定的符号连接起来
语法：连接符.join(字符串)
'''
a=['a','v','f']
b='*'
print(b.join(a))