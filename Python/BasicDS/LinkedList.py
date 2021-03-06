# coding=utf-8
# @Time       : 2020/2/12
# @Author     : Wang Xiaoxiao
# @University : Dalian University of Technology
# @FileName   : LinkedList.py
# @Software   : PyCharm
# @github     : https://github.com/i-love-linux/BasicDataStructure


class LinkedList:

    class __Node:
        def __init__(self, element=None, next=None):
            self.e = element
            self.next = next
    """
    时间复杂度分析：
    添加操作：addLast(e):O(n)    addFirst(e):O(1)    add(index, e):O(n/2)=O(n)
    删除操作：removeLast(e):O(n)    removeFirst(e):O(1)    remove(index, e):O(n/2)=O(n)
    修改操作：set(index, e):O(n)
    查找操作：get(index):O(n)    contains(e):O(n)
    """
    def __init__(self):
        self.__dummyHead = self.__Node()
        self.__size = 0

    # 获取链表中的元素的个数
    def getSize(self):
        return self.__size

    # 判断链表是否为空
    def isEmpty(self):
        return self.__size == 0

    # 在链表的index(0-based)位置添加新的元素e
    # 在链表中不是一个常用的操作，练习用
    def add(self, index, e):
        assert not (index < 0 or index > self.__size), "Add failed. Illegal index."

        prev = self.__dummyHead
        for i in range(index):
            prev = prev.next

        # node = self.__Node(element=e)
        # node.next = prev.next()
        # prev.next = node
        prev.next = self.__Node(e, prev.next)
        self.__size += 1

    # 在链表头添加元素
    def addFirst(self, e):
        self.add(0, e)

    # 在链表的末尾添加新的元素e
    def addLast(self, e):
        self.add(self.__size, e)

    # 获得链表的第index(0-based)个位置的元素
    # 在链表中不是一个常用的操作，练习用
    def get(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Add failed. Illegal index.")

        cur = self.__dummyHead.next
        for i in range(index):
            cur = cur.next
        return cur.e

    # 获得链表的第一个元素
    def getFirst(self):
        return self.get(0)

    # 获取链表的最后一个元素
    def getLast(self):
        return self.get(self.__size - 1)

    # 修改链表的第ndex(0-based)个位置的元素为e
    # 在链表中不是一个常用的操作，练习用
    def set(self, index, e):
        assert not (index < 0 or index >= self.__size), "Add failed. Illegal index."
        cur = self.__dummyHead.next
        for i in range(index):
            cur = cur.next
        cur.e = e

    # 在链表中查找是否有元素e
    def contains(self, e):
        cur = self.__dummyHead
        while cur is not None:
            if cur.e == e:
                return True
            cur = cur.next
        return False

    # 从链表删除index(0-based)位置的元素，返回删除的元素
    # 在链表中不是一个常用的操作，练习用
    def remove(self, index):
        assert not (index < 0 or index >= self.__size), "Add failed. Illegal index."
        prev = self.__dummyHead
        for i in range(index):
            prev = prev.next

        retNode = prev.next
        prev.next = retNode.next
        retNode.next = None
        self.__size -= 1

        retValue = retNode.e
        del(retNode)
        return retValue

    # 从链表中删除第一个元素，返回删除的元素
    def removeFirst(self):
        return self.remove(0)

    # 从链表中删除最后一个元素，返回删除的元素
    def removeLast(self):
        return self.remove(self.__size - 1)

    # 从链表中删除元素e
    def removeElement(self, e):
        prev = self.__dummyHead
        while prev.next is not None:
            if prev.next.e == e:
                break
            prev = prev.next

        if prev.next is not None:
            delNode = prev.next
            prev.next = delNode.next
            del delNode
            self.__size -= 1

    def __str__(self):
        return self.getString()

    def getString(self):
        res = ""
        cur = self.__dummyHead.next
        while cur is not None:
            res = res + str(cur.e) + "->"
            cur = cur.next
        res += "NULL"
        return res




