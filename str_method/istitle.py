#-*-  coding=utf-8 -*-
print(help(str.istitle))
'''
istitle(...)
    S.istitle() -> bool
    
    Return True if S is a titlecased string and there is at least one
    character in S, i.e. uppercase characters may only follow uncased
    characters and lowercase characters only cased ones. Return False
    otherwise.

None
istitle方法用于检测字符串中所有的单词的首字母是否为大写，且其他字母为小写。
'''
a='SayEca'
print(a.istitle())
b='Say Eca'
print(b.istitle())