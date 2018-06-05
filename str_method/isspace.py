#-*-  coding=utf-8 -*-
print(help(str.isspace))
'''
isspace(...)
    S.isspace() -> bool
    
    Return True if all characters in S are whitespace
    and there is at least one character in S, False otherwise.

None
isspace方法用来检测字符串是否只由空格组成
'''
a='fffsdffaf'
print(a.isspace())
b='            '
print(b.isspace())