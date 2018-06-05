#-*- coding=utf-8 -*-
print(help(str.center))
'''
center(...)
    S.center(width[, fillchar]) -> string
    
    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)
center的作用是将定义的原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格，其填充字符可自定义
'''
print('*'*50)
s='yaxuan'
m=s.center(10)
print(m)
print('*'*50)
a='FuzzTestPoc'
b=a.center(20,'*')
print(b)