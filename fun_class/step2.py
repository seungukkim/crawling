# -*- coding: cp949 -*-


# 함수에서 list 다룰 때 주의점
# list vs tuple
def list_a(var=[]):
    var.append(1)
    return var

def list_b(var=None):
    if var is None:
        var=[]
    var.append(1)
    return var

if __name__ =="__main__":
    print(list_a())
    print(list_a())
    print(list_b())
    print(list_a())
    print('---------')
    print(list_b())
    print(list_b())
    print(list_b())
    