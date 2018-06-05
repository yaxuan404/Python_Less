#-*- coding=utf-8 -*-
print(help(str.find))
'''
find(...)
    S.find(sub [,start [,end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

None
find方法的作用是用来查找指定的字符在字符串中的位置,查询不到个返回-1

'''
a='yaxuan'
print(a.find('x',0,5))
print(a.find('1'))