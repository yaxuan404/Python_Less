#-*- coding=utf-8 -*-
print(help(str.isdigit))
'''
isdigit(...)
    S.isdigit() -> bool
    
    Return True if all characters in S are digits
    and there is at least one character in S, False otherwise.

None
isdigit方法用来检测字符串是否只有数字组成
'''
s='12324'
print(s.isdigit())
a='yaxuan99'
print(a.isdigit())