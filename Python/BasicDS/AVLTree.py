# coding=utf-8


class AVLTree:
    """
    时间复杂度分析(平均)：n为元素个数
    增 add：O(logn)
    删 remove：O(logn)
    改 set：O(logn)
    查 get：O(logn)      contains：O(logn)
    """
    class __Node:
        def __init__(self, key=None, value=None, left=None, right=None):
            self.key = key  # 键
            self.value = value  # 值
            self.left = left  # 左子树
            self.right = right  # 右子树
            self.height = 1  # 节点所在的高度，叶节点为1

    def __init__(self):
        self.__root = None
        self.__size = 0
        self.__treeString = ""

    # 获取二分搜索树中的元素的个数
    def getSize(self):
        return self.__size

    # 判断二分搜索树是否为空
    def isEmpty(self):
        return self.__size == 0

    # 判断该二叉树是否是一棵二分搜索树
    def isBST(self):
        keys = []
        self.__inOrder(self.__root, keys)
        for i in range(1, len(keys)):
            if keys[i-1] > keys[i]:
                return False
        return True

    def __inOrder(self, node, keys):
        if node == None:
            return
        self.__inOrder(node.left, keys)
        keys.append(node.key)
        self.__inOrder(node.right, keys)

    # 判断该二叉树是否是一棵平衡二叉树
    def isBalanced(self):
        return self.__isBalanced(self.__root)

    # 判断以node为根的二叉树是否是一棵平衡二叉树，递归算法
    def __isBalanced(self, node):
        if node == None:
            return True

        balanceFactor = self.__getBlanceFactor(node)
        if abs(balanceFactor) > 1:
            return False
        return self.__isBalanced(node.left) and self.__isBalanced(node.right)

    # 获取节点node的平衡因子
    def __getBlanceFactor(self, node):
        if node == None:
            return 0
        return self.__getHeight(node.left) - self.__getHeight(node.right)

    # 获取节点的高度值
    def __getHeight(self, node):
        if node == None:
            return 0
        return node.height

    # 对节点y进行向右旋转操作(因为只添加一个节点，所以y的平衡因子为2)，返回旋转后新的根节点x
    #        y                              x
    #       / \                           /   \
    #      x   T4     向右旋转 (y)        z     y
    #     / \       - - - - - - - ->    / \   / \
    #    z   T3                       T1  T2 T3 T4
    #   / \
    # T1   T2
    def __RightRotate(self, y):
        # 暂存信息
        x = y.left
        T3 = x.right

        # 向右旋转过程
        x.right = y
        y.left = T3

        # 更新height
        y.height = max(self.__getHeight(y.left), self.__getHeight(y.right)) + 1
        x.height = max(self.__getHeight(x.left), self.__getHeight(x.right)) + 1

        return x

    # 对节点y进行向左旋转操作(因为只添加一个节点，所以y的平衡因子为2)，返回旋转后新的根节点x
    #    y                             x
    #  /  \                          /   \
    # T1   x      向左旋转 (y)       y     z
    #     / \   - - - - - - - ->   / \   / \
    #   T2  z                     T1 T2 T3 T4
    #      / \
    #     T3 T4
    def __LeftRotate(self, y):
        # 暂存信息
        x = y.right
        T2 = x.left

        # 向右旋转过程
        x.left = y
        y.right = T2

        # 更新height
        y.height = max(self.__getHeight(y.left), self.__getHeight(y.right)) + 1
        x.height = max(self.__getHeight(x.left), self.__getHeight(x.right)) + 1

        return x

    # 向二分搜索树中添加元素(key, value)
    def add(self, key, value):
        self.__root = self.__add(self.__root, key, value)

    # 向以node为根节点的二分搜索树中添加元素(key, value)，递归算法
    # 返回插入新节点后二分搜索树的根
    def __add(self, node, key, value):
        if node == None:
            self.__size += 1
            return self.__Node(key=key, value=value)

        if key < node.key:
            node.left = self.__add(node.left, key, value)
        elif key > node.key:
            node.right = self.__add(node.right, key, value)
        else:  # key == node.key
            node.value = value

        # 更新height
        node.height = 1 + max(self.__getHeight(node.left), self.__getHeight(node.right))

        # 计算平衡因子
        balanceFactor = self.__getBlanceFactor(node)
        # if abs(balanceFactor) > 1:
        #     print("unbalanced : ", balanceFactor)

        # 平衡维护
        if balanceFactor > 1 and self.__getBlanceFactor(node.left) >= 0:
            return self.__RightRotate(node)
        if balanceFactor < -1 and self.__getHeight(node.right) <= 0:
            return self.__LeftRotate(node)

        return node

    def remove(self, key):
        node = self.__getNode(self.__root, key)
        if node != None:
            self.__root = self.__remove(self.__root, key)
            return node.value
        return None

    # 返回以node为根的二分搜索树的最小值所在的节点，递归算法
    def __minimum(self, node):
        if node.left == None:
            return node
        return self.__minimum(node.left)

    # 删除以node为根的二分搜索树中的最小节点
    # 返回删除节点后新的二分搜索树的根
    def __removeMin(self, node):
        if node.left == None:
            rightNode = node.right
            # node.right = None
            del node
            self.__size -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    # 从二分搜索树中删除键为e的节点，递归算法
    # 返回删除节点后新的二分搜索树的根
    def __remove(self, node, key):
        if node == None:
            return None

        if key < node.key:
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__remove(node.right, key)
            return node
        else:  # key == node.key
            # 待删除节点左子树为空的情况
            if node.left == None:
                rightNode = node.right
                # node.right = None
                del node
                self.__size -= 1
                return rightNode
            # 待删除节点右子树为空的情况
            if node.right == None:
                leftNode = node.left
                # node.left = None
                del node
                self.__size -= 1
                return leftNode
            # 待删除节点左右子树均不为为空的情况
            # 找到比待删除节点大的最小节点, 即待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            successor = self.__minimum(node.right)  # 获取node右子树最小值
            successor.right = self.__removeMin(node.right)  # 删除node右子树最小值，同时挂接右子树
            successor.left = node.left  # 挂接左子树
            node.left = node.right = None
            # del node  # 删除node

            return successor

    def set(self, key, value):
        node = self.__getNode(self.__root, key)
        if node == None:
            raise Exception(str(key) + " does't exist!")
        node.value = value

    def get(self, key):
        node = self.__getNode(self.__root, key)
        if node == None:
            return None
        else:
            return node.value

    def contains(self, key):
        return self.__getNode(self.__root, key) != None

    # 返回以node为根节点的二分搜索树中，key所在的节点
    def __getNode(self, node, key):
        if node == None:
            return None

        if key == node.key:
            return node
        elif key < node.key:
            return self.__getNode(node.left, key)
        else:  # key > node.key
            return self.__getNode(node.right, key)

