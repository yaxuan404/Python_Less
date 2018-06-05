#-*- coding=utf-8 -*-
print(help(str.decode))
'''
decode(...)
    S.decode([encoding[,errors]]) -> object
    
    Decodes S using the codec registered for encoding. encoding defaults
    to the default encoding. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
    as well as any other name registered with codecs.register_error that is
    able to handle UnicodeDecodeErrors.
    decode方法的作用是将字符以encoding 指定的编码格式解码字符串。默认编码为字符串编码。
    encoding -- 要使用的编码，如"UTF-8"。 
	errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

'''
print('*'*50)
a='WWF4dWFuIGlzIGhhbmRzb21lIHRoYW7vvIHvvIHvvIE=iy'
b=a.decode('base64','strict')
print(b)