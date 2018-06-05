#-*- coding=utf-8 -*-
print(help(str.count))
'''
count(...)
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are interpreted
    as in slice notation.
count的作用是统计字符串中定义的字符个数,可选参数为在字符串搜索的开始与结束位置。
'''
a='sahddasdkd'
b=a.count('s',0,10)
print(b)