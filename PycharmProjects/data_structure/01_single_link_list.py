class Node(object):
    """单个节点 """
    def __init__(self, elem):
        # 该节点存放的数据
        self.elem = elem
        # 指向下个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """求长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部添加元素，尾插发"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

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
        pre = None
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    self.__head == cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
        return False

    def search(self, item):
        """查看节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
