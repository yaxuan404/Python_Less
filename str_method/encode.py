#-*- coding=utf-8 -*-
print(help(str.encode))
'''
encode(...)
    S.encode([encoding[,errors]]) -> object
    
    Encodes S using the codec registered for encoding. encoding defaults
    to the default encoding. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that is able to handle UnicodeEncodeErrors.
    encode方法和decode方法的作用一样，decode是用来解密，encode是用来加密
'''
print('*'*50)
a='yaxuan is mam'
b=a.encode('base64','strict')
print(b)