#!/usr/bin/env python3
# coding:utf-8

def BinaryTree(item):
    return [item, [], []]


def insertLeft(tree, item):
    leftSubtree = tree.pop(1)
    if leftSubtree:
        tree.insert(1, [item, leftSubtree, []])
    else:
        tree.insert(1, [item, [], []])
    return tree


def insertRight(tree, item):
    rightSubtree = tree.pop(2)
    if rightSubtree:
        tree.insert(2, [item, [], rightSubtree])
    else:
        tree.insert(2, [item, [], []])
    return tree


def getLeftChild(tree):
    return tree[1]


def getRightChild(tree):
    return tree[2]


tree = BinaryTree('a')
insertLeft(tree, 'b')
insertRight(tree, 'c')
insertRight(getLeftChild(tree), 'd')
insertLeft(getLeftChild(tree), 'e')
insertRight(getRightChild(tree), 'f')


# print(tree)

class BinaryTree:
    def __init__(self, item):
        self.key = item
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, item):
        if self.leftChild == None:
            self.leftChild = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, item):
        if self.rightChild == None:
            self.rightChild = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.rightChild = self.rightChild
            self.rightChild = t


tree = BinaryTree('a')
tree.insertLeft('b')
