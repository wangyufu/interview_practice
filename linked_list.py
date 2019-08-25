#!/usr/bin/env python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def add_left(self,newdata):
        old_node = self.headval
        self.headval = Node(newdata)
        self.headval.nextval = old_node

    # 在链表末尾添加一个新的node
    def append(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    # 打印链表
    def show(self):
        printval = self.headval
        while printval:
            print(printval.dataval)
            printval = printval.nextval


li = SLinkedList()
li.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# 连接第一第二个节点
li.headval.nextval = e2

# 连接第二第三个节点
e2.nextval = e3

# print(e2.nextval)
# #结果为e3内存地址<__main__.Node object at 0x0000001A0F9644BE0>
# print(e2.nextval.dataval)
#结果为e3所代表的值Wed
li.append('Thu')
li.add_left('A')
li.show()