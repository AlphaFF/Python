#!/usr/bin python3
# coding:utf-8

# import re
#
# line = 'booooooobby123'
# regex_str = '(b.*b)(.*)'
# match_obj = re.match(regex_str,line)
#
# if match_obj:
# 	print(match_obj.group(0))
# 	print(match_obj.group(1))
# 	print(match_obj.group(2))

class Root():
    def __init__(self):
        print("this is root")

class B(Root):
    def __init__(self):
        print("enter B")
        print(self)
        super(B,self).__init__()
        print('leave B')

class C(Root):
    def __init__(self):
        print("enter C")
        super(C,self).__init__()
        print("leave C")

class D(B,C):
    print("enter D")
    pass

if __name__ == "__main__":
    d = D()
    print(d.__class__.__mro__)
    print(d.__class__.mro())
    print(d.__class__.__name__)


