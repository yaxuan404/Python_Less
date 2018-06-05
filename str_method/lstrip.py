#-*- coding=utf-8 -*-
print(help(str.lstrip))
'''
lstrip(...)
    S.lstrip([chars]) -> string or unicode
    
    Return a copy of the string S with leading whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

None
lstrip方法用于截掉字符串左边的空格或指定字符。chars指截取的自定义字符
'''
a='                  yaxuan!!!!!'
print(a)
print(a.lstrip())
b='666yaxuan!!!!!'
print(b)
print(b.lstrip('6'))