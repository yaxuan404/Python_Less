#-*-  coding=utf-8 -*-
print(help(str.translate))
'''
translate(...)
    S.translate(table [,deletechars]) -> string
    
    Return a copy of the string S, where all characters occurring
    in the optional argument deletechars are removed, and the
    remaining characters have been mapped through the given
    translation table, which must be a string of length 256 or None.
    If the table argument is None, no translation is applied and
    the operation simply removes the characters in deletechars.

None
translate方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。
'''
from string import maketrans   # 引用 maketrans 函数
a='yaxuan';
b='808099';
c=maketrans(a,b);
str='ma am';
print(str.translate(c));