#-*- coding=utf-8 -*-
print(help(str.index))
'''
index(...)
    S.index(sub [,start [,end]]) -> int
    
    Like S.find() but raise ValueError when the substring is not found.

None
index方法是用来检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
'''
a='yaxuan'
print(a.index('x',0,5))
print(a.index('1',0,20))