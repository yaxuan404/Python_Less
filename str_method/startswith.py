#-*- coding=utf-8 -*-
print(help(str.startswith))
'''
startswith(...)
    S.startswith(prefix[, start[, end]]) -> bool
    
    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.

None
startswith方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 start 和 end 指定值，则在指定范围内检查。
'''
a='yaxuan';
print(a.startswith("y"));
print(a.startswith("x"));
str = "this is string example....wow!!!";
print str.startswith( 'this' );
print str.startswith( 'is', 2, 4 );
print str.startswith( 'this', 0, 4 );