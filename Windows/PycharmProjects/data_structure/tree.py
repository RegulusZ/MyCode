# coding:utf-8


class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        if self.root is None:
            self.root = Node(item)
            return
        queue = [self.root]
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur.lchild is not None:
                queue.append(cur.lchild)
            else:
                cur.lchild = Node(item)
                return

            if cur.rchild is not None:
                queue.append(cur.rchild)
            else:
                cur.rchild = Node(item)
                return

    def travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while len(queue) > 0:
            cur = queue.pop(0)
            print(cur.elem)
            if cur.lchild is not None:
                queue.append(cur.lchild)

            if cur.rchild is not None:
                queue.append(cur.rchild)


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.travel()
