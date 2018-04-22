#! /usr/bin/env python3
# coding:utf-8

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    # same tree
    def isSameTree(self, p, q):
        if p and q:
            return p.key == q.key and self.isSameTree(p.leftChild, q.leftChild) and self.isSameTree(p.rightChild,
                                                                                                    q.rightChild)
        return p is q

    # symmetric tree
    def isSymmetricTree(self, rootObj):
        if rootObj is None:
            return True
        stack = [(rootObj.leftChild, rootObj.rightChild)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.key == right.key:
                stack.append((left.leftChild, right.rightChild))
                stack.append((left.rightChild, right.leftChild))
            else:
                return False
        return True

    # maximum depth
    def maxDepth(self, rootObj):
        return 1 + max(map(self.maxDepth, (rootObj.leftChild, rootObj.rightChild))) if rootObj else 0

    # minimum depth
    def minDepth(self, rootObj):
        if rootObj == None:
            return 0
        if rootObj.leftChild == None or rootObj.rightChild == None:
            return self.minDepth(rootObj.leftChild) + self.minDepth(rootObj.rightChild) + 1
        return 1 + min(map(self.minDepth, (rootObj.leftChild, rootObj.rightChild)))

    # traversal (dfs)
    def traversal(self, rootObj):
        stack = [(rootObj, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.key)
                stack.append((node.rightChild), level + 1)
                stack.append((node.leftChild), level + 1)
        return res

    # convert sorted array to binary tree
    def sortedArrayToBST(self, num):
        if not num:
            return None
        mid = len(num) // 2
        root = BinaryTree(num[mid])
        root.leftChild = self.sortedArrayToBST(num[:mid])
        root.rightChild = self.sortedArrayToBST(num[mid + 1:])
        return root

    # balanced binary tree
    def isBalanced(self, root):
        def check(root):
            if root is None:
                return 0
            left = check(root.leftChild)
            right = check(root.rightChild)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

    # path sum
    def hasPathSum(self, rootObj, sum):
        if not rootObj:
            return False
        if not rootObj.leftChild and not rootObj.rightChild and rootObj.key == sum:
            return True
        sum -= rootObj.key
        return self.hasPathSum(rootObj.leftChild, sum) or self.hasPathSum(rootObj.rightChild, sum)

    # path sum III
    def hasPathSum1(self, rootObj, sumNum):
        if not rootObj:
            return 0
        res = 0
        t = sumNum
        sumNum -= rootObj.key
        if sumNum < 0:
            sumNum = t
            self.hasPathSum1(rootObj.leftChild, sumNum)
            self.hasPathSum1(rootObj.rightChild, sumNum)
        if sumNum == 0:
            res += 1
        if sumNum > 0:
            self.hasPathSum1(rootObj.leftChild, sumNum)
            self.hasPathSum1(rootObj.rightChild, sumNum)
        return res

    # invert a binary
    def invert(self, rootObj):
        if not rootObj:
            return
        stack = [(rootObj.leftChild, rootObj.rightChild)]
        while stack:
            left, right = stack.pop()
            rootObj.leftChild = right
            rootObj.rightChild = left
            stack.append(right.leftChild, right.rightChild)
            stack.append(left.leftChild, left.rightChild)
        return rootObj

    # binary tree paths
    def binaryTreePaths(self, rootObj):
        if not rootObj:
            return []
        res = []
        stack = [(rootObj, '')]
        while stack:
            node, ls = stack.pop()
            if not node.leftChild and not node.rightChild:
                res.append(ls + str(node.key))
            if node.rightChild:
                stack.append((node.rightChild, ls + str(node.key) + '->'))
            if node.leftChild:
                stack.append((node.leftChild, ls + str(node.key) + '->'))
        return res

    # sum of left leaves
    def sumOfLeftLeaves(self, rootObj):
        if not rootObj:
            return 0
        num = 0
        stack = [(rootObj, num)]
        while stack:
            node, num = stack.pop()
            if node.leftChild:
                num += int(node.leftChild.key)
                stack.append((node.leftChild, num))
            if node.rightChild:
                stack.append((node.rightChild, num))
                # if not node.leftChild and not node.rightChild:
                # 	continue
        return num

    # ?
    def sumOfLeftLeaves1(self, rootObj):
        if not rootObj: return 0
        if rootObj.leftChild and not rootObj.leftChild.leftChild and not rootObj.leftChild.rightChild:
            return rootObj.key + self.sumOfLeftLeaves1(rootObj.rightChild)
        return self.sumOfLeftLeaves1(rootObj.leftChild) + self.sumOfLeftLeaves1(rootObj.rightChild)

    # convert bst to greater tree ?
    def convertBST(self, root):
        def visit1(root):
            if root:
                visit1(root.leftChild)
                vals.append(root.key)
                visit1(root.rightChild)

        vals = []
        visit1(root)
        self.s = 0

        def visit2(root):
            if root:
                visit2(root.rightChild)
                self.s += vals.pop()
                root.key = self.s
                visit2(root.leftChild)

        visit2(root)

        return root

    # diameter binary of tree
    def diameterOfBinaryTree(self, root):
        self.best = 1

        def depth(root):
            if not root: return 0
            ansL = depth(root.leftChild)
            ansR = depth(root.rightChild)
            self.best = max(self.best, ansL + ansR + 1)
            return 1 + max(ansL, ansR)

        depth(root)
        return self.best - 1


if __name__ == '__main__':
    t = BinaryTree(1)
    t.insertLeft(2)
    t.insertRight(3)
    print(t.getLeftChild().key)
    t.getLeftChild().insertLeft(4)
    t.getLeftChild().insertRight(5)
    print(t.getLeftChild().getLeftChild().key)
    t.diameterOfBinaryTree(t)