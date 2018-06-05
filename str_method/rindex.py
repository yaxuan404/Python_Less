#-*- coding=utf-8 -*-
print(help(str.rindex))
'''
rindex(...)
    S.rindex(sub [,start [,end]]) -> int
    
    Like S.rfind() but raise ValueError when the substring is not found.

None
rindex方法用于返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[start:end]设置查找的区间。
'''
a='yaxuan'
b='a'
print(a.rindex(b))#从右到左依次匹配
print(a.index(b))#从左到右依次匹配