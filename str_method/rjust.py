#-*- coding=utf-8 -*-
print(help(str.rjust))
'''
rjust(...)
    S.rjust(width[, fillchar]) -> string
    
    Return S right-justified in a string of length width. Padding is
    done using the specified fill character (default is a space)

None
rjust方法是用指定的长度返回原字符串，字符长度不够默认用空格填充，填充字符可自定义,和ljust不同的是他从左到右填充
'''
a='yaxuan'
print(a.rjust(3))
print(a.rjust(10,'*'));
print(a.ljust(10,"*"));