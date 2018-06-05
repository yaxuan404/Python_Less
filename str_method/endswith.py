#-*- coding=utf-8 -*-
print(help(str.endswith))
'''
endswith(...)
    S.endswith(suffix[, start[, end]]) -> bool
    
    Return True if S ends with the specified suffix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    suffix can also be a tuple of strings to try.
endswith方法用来判断字符串是否以指定的后缀格式结尾，返回即为true，否则为false
'''
a='yaxuan'
s='an'
b=a.endswith(s,2,5)
print(b)
print(a.endswith(s,2,6))
