#-*- coding=utf-8 -*-
print(help(str.strip))
'''
strip(...)
    S.strip([chars]) -> string or unicode
    
    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

None
strip方法用于移除字符串头尾指定的字符（默认为空格或换行符）。
'''
a='****yaxuan****';
print(a.strip('*'));
a='     yaxuan      ';
print(a.strip());