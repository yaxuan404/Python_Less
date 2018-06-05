#-*- coding=utf-8 -*-
print(help(str.splitlines))
'''
splitlines(...)
    S.splitlines(keepends=False) -> list of strings
    
    Return a list of the lines in S, breaking at line boundaries.
    Line breaks are not included in the resulting list unless keepends
    is given and true.

None
splitlines方法按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
'''
a='ya\nxuan';
print(a.splitlines())
print(a.splitlines(True))