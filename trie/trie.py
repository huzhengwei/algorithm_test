#!/usr/bin/python
#coding:utf8

class Node(object):
    def __init__(self, c = None):
        self.c = c
        self.count = 0
        self.value = 0
        self.childs = {}

class Trie(object):
    def __init__(self):
        self.root = Node()
    def insert(self, keystr, value = 1):
        put(self.root, keystr, value)

    def put(node, keystr, value):
        head = keystr[0]
        if head not in node.childs:
            node = Node(head)

        node.count += 1
        if len(keystr) == 1:
            node.value = value
        else:
            put(node.childs[head], keystr[1:])

    def search(node, keystr):
        head = keystr[0]
        if len(keystr) == 1 or head not in node.childs:
            return node;
        else:
            search(node.childs[head], keystr[1:])

    def size(self, keystr):
        end = search(self.root, keystr)
        return end.count;

if __name__ == '__main__':
    trie = Trie()
    size = input()
    print(size)
    for i in range(size):
        trie.insert(raw_input())

    samsize = input()
    for i in range(samsize):
        print(trie.size(raw_input()))




