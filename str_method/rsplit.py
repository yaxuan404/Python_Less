#-*- coding=utf-8 -*-
print(help(str.rsplit))
'''
rsplit(...)
    S.rsplit([sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string S, using sep as the
    delimiter string, starting at the end of the string and working
    to the front.  If maxsplit is given, at most maxsplit splits are
    done. If sep is not specified or is None, any whitespace string
    is a separator.

None
rsplit方法通过指定分隔符对字符串从右到左进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串.
参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。
'''
a='ya/nxuan/nis/nvery/ngood';
print(a.split('/n',1))
print(a.rsplit('/n',1))