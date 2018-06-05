#-*- coding=utf-8 -*-
print(help(str.replace))
'''
replace(...)
    S.replace(old, new[, count]) -> string
    
    Return a copy of string S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.

None
replace方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
'''
a='this is yaxuan88,he is very cool!!!'
print(a.replace('is','was'))
print(a.replace('is','was',2))