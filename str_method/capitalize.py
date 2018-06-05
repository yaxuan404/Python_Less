#-*- coding=utf-8 -*-
print(help(str.capitalize))
'''
capitalize(...)
    S.capitalize() -> string
    
    Return a copy of the string S with only its first character
    capitalized.
capitalize的作用是将变量的第一个字符变成大写，后面的全部变成小写
'''
print('*'*50)
a='r,B'
b=a.capitalize()
print(b)
print('*'*50)
s='n,B,n,v,b,n,m'
m=s.capitalize()
print(m)