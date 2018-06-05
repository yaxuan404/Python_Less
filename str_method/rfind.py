#-*- coding=utf-8 -*-
print(help(str.rfind))
'''
rfind(...)
    S.rfind(sub [,start [,end]]) -> int
    
    Return the highest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.

None
rfind方法用于返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
'''
a='yaxuan'
b='v'
s='x'
print(a.rfind(b))
print(a.find(b))
print(a.rfind(s,0,4))
print(a.find(s,0,4))
