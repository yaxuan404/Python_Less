#-*- coding=utf-8 -*-
print(help(str.split))
'''
split(...)
    S.split([sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are removed
    from the result.

None
split方法通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串.
参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。
'''
a='ya/nxuan/nis/nvery/ngood';
print(a.split('/n',1))
print(a.rsplit('/n',1))