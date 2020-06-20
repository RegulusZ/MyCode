class Node(object):
    """单个节点 """
    def __init__(self, elem):
        # 该节点存放的数据
        self.elem = elem
        # 指向下个节点的标识
        self.next = None


class SingleLinkList(object):
    """单循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node is not None:
            node.next = node

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None
 
    def length(self):
        """求长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 1
        if self.is_empty():
            return 0
        else:
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        """遍历"""
        cur = self.__head
        if self.is_empty():
            return
        else:
            while cur.next != self.__head:
                print(cur.elem, end=" ")
                cur = cur.next
            print(cur.elem)
            print("")

    def add(self, item):
        """头部添加元素，头插法"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node

    def append(self, item):
        """尾部添加元素，尾插发"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素
        :param item:节点数据
        :param pos:插入位置，从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1
            # 当循环退出后，pre指向pos-1位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除指定元素"""
        if self.is_empty():
            return False
        pre = None
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                # 此节点是头节点的情况
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 只有一个节点
                self.__head = None
            else:
                pre.next = cur.next
            return True
        else:
            return False

    def search(self, item):
        """查看节点是否存在"""
        cur = self.__head
        if self.is_empty():
            return  False
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        else:
            return False
