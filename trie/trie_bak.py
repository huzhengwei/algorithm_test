#!/usr/bin/python
#coding:utf8

class Node(object):
    def __init__(self, c = None):
        # self.c = c
        self.count = 0
        # self.value = 0
        self.childs = {}

class Trie(object):
    def __init__(self):
        self.root = Node()
    def insert(self, keystr, value = 1):
        self._put(self.root, keystr, value)

    def _put(self, node, keystr, value):
        strindex = 0
        len_key = len(keystr)
        while (len_key != strindex):
            head = keystr[strindex]
            node.count += 1
            if head not in node.childs:
                node.childs[head] = Node()

            # keystr = keystr[1:]
            strindex += 1
            node = node.childs[head]

        # node.value = value
        node.count += 1

    def _put_recurse(self, node, keystr, value):
        head = keystr[0]
        node.count += 1
        if head not in node.childs:
            node.childs[head] = Node()

        if len(keystr) == 1:
            node.childs[head].value = value
            node.childs[head].count += 1;
        else:
            self._put(node.childs[head], keystr[1:], value)

    def _search(self, node, keystr):
        strindex = 0
        head = keystr[strindex]
        len_key = len(keystr)
        while(head in node.childs):
            node = node.childs[head]
            # keystr = keystr[1:]
            strindex += 1
            if(len_key == strindex):
                return node
            head = keystr[strindex]

        return None
    def _search_recurse(self, node, keystr):
        head = keystr[0]
        if head in node.childs:
            if len(keystr) == 1:
                return node.childs[head]
            else:
                return self._search(node.childs[head], keystr[1:])
        else:
            return None

    def size(self, keystr):
        end = self._search(self.root, keystr)
        if not end:
            return 0
        return end.count

if __name__ == '__main__':
    trie = Trie()
    import pudb; pudb.set_trace()  # XXX BREAKPOINT
    size = input()
    for i in xrange(size):
        trie.insert(raw_input())

    samsize = input()
    for i in xrange(samsize):
        print(trie.size(raw_input()))




