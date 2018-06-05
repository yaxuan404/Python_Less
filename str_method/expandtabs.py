#-*- coding=utf-8 -*-
print(help(str.expandtabs))
'''
expandtabs(...)
    S.expandtabs([tabsize]) -> string
    
    Return a copy of S where all tab characters are expanded using spaces.
    If tabsize is not given, a tab size of 8 characters is assumed.

None
expandtabs方法的作用是将字符串中的tab符号('\t')转换成空格，tab 符号('\t')默认的空格数是 8
'''
a='ya\txuan'
print(a.expandtabs(5))