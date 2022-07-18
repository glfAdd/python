"""
container: 容器, 用来储存元素的一种数据结构, 如 list，set，dict，str 等
可迭代对象: 实现了 __iter__ 方法的对象
迭代器: 实现了 __next__ 方法的对象
生成器:


for 循环原理
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
"""


class Test1:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 10:
            raise StopIteration
        else:
            self.num += 1
            return self.num


class Test2:
    def __init__(self, num):
        self.num = num

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self.num > 10:
            raise StopIteration
        else:
            self.num += 1
            return self.num


if __name__ == '__main__':
    t = Test1(7)
    for i in Test1(1):
        print(i)
    for i in Test2(1):
        print(i)
    # for i in range(7):
    #     print(t.__next__())
