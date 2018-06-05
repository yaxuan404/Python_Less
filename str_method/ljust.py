#-*-  coding=utf-8 -*-
print(help(str.ljust))
'''
ljust(...)
    S.ljust(width[, fillchar]) -> string
    
    Return S left-justified in a string of length width. Padding is
    done using the specified fill character (default is a space).

None
ljust方法是用指定的长度返回原字符串，字符长度不够默认用空格填充，填充字符可自定义
'''
a='yaxuan cool'
print(a.ljust(50))       #默认填充为空格
print(a.ljust(50,'*'))   #填充字符定义为*