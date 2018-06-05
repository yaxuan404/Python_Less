#-*- coding=utf-8 -*-
print(help(str.zfill))
'''
zfill(...)
    S.zfill(width) -> string
    
    Pad a numeric string S with zeros on the left, to fill a field
    of the specified width.  The string S is never truncated.

None
zfill方法返回指定长度的字符串，原字符串右对齐，前面填充0,不可指定填充字符
'''
a='yaxuan';
print(a.zfill(10));
print(a.zfill(20));