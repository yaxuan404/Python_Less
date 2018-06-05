#-*- coding=utf-8 -*-
print(help(str.rpartition))
'''
rpartition(...)
    S.rpartition(sep) -> (head, sep, tail)
    
    Search for the separator sep in S, starting at the end of S, and return
    the part before it, the separator itself, and the part after it.  If the
    separator is not found, return two empty strings and S.

None
rpartition方法类似于 partition方法，只是该方法是从目标字符串的末尾也就是右边开始搜索分割符。。
如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串
'''
a='yaxuan';
b='www.yaxuansec.top';
print(a.rpartition('x'));
print(a.partition('x'));
print(b.rpartition('.'));
print(b.partition('.'));
