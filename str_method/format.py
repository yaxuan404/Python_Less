#-*- coding=utf-8 -*-
print(help(str.format))
'''
format(...)
    S.format(*args, **kwargs) -> string
    
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').

None
format方法的作用是格式化字符串，其中有两种定义：
1.>>>"{} {}".format("ya", "xuan")    # 不设置指定位置，按默认顺序
'ya xuan'
 
2.>>> "{0} {1}".format("ya", "xuan")  # 设置指定位置
'ya xuan'
'''
print("{0}{1}".format("ya","xuan"))