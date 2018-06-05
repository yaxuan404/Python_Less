#-*- coding=utf-8 -*-
print(help(str.isalnum))
'''
isalnum(...)
    S.isalnum() -> bool
    
    Return True if all characters in S are alphanumeric
    and there is at least one character in S, False otherwise.

None
isalnum方法用来检测字符串是否由数字和字符组成，如果字符串中至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
'''
a='yaxuan'
print(a.isalnum())
b='yaxuan is man'
print(b.isalnum())#字符串中包含空格
