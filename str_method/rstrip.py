#-*- coding=utf-8 -*-
print(help(str.rstrip))
'''
rstrip(...)
    S.rstrip([chars]) -> string or unicode
    
    Return a copy of the string S with trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

None
rstrip方法指的是删除 string 字符串末尾的指定字符（默认为空格）
'''
a='yaxuan!!!1';
print(a.rstrip("!"));
print(a.strip("!"));

