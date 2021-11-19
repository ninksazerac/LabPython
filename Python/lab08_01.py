'''
Huffman Encoding
ให้นักศึกษาเขียนโปรแกรมในการเข้ารหัส Huffman (บีบอัดข้อมูล) โดยใช้ Tree และแสดงผลตามตัวอย่าง
#อ่านวิธีการเข้ารหัสได้ที่ http://datastructurealgori.blogspot.com/2017/06/huffmans-code.html
'''
class Node:
    def __init__(self, new_item, frequency):
        self.item = new_item
        self.frequency = frequency
        self.left = None
        self.right = None

    def __len__(self):
        return self.frequency


class Stack:
    def __init__(self):
        self.items = []

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def deq(self):
        if self.items:
            return self.items.pop(0)
        return None

    def top(self):
        if self.items:
            return self.items[-1]
        return None

    def head(self):
        if self.items:
            return self.items[0]
        return None


class Huffman:
    def __init__(self):
        self.root = None
        self.items = []
        self.w = {}

    def prepare(self, inputlist):
        l = sorted(inputlist)
        dic = {i: l.count(i) for i in l}
        dic = dict(sorted(dic.items(), key=lambda x: x[1]))
        keys = list(dic.keys())
        sort = [Node(key, dic[key]) for key in keys[::-1]]
        while len(sort):
            self.items.append(sort[0])
            for j in sort[1:]:
                if sort[0].frequency == j.frequency:
                    self.items.append(j)
                    sort.remove(j)
            sort.remove(sort[0])
    def insert(self):
        new_node = Node('*',self.items[-1].frequency + self.items[-2].frequency)
        new_node.left = self.items.pop()
        new_node.right = self.items.pop()
        l = []
        l += [i for i in self.items if i.frequency > new_node.frequency]
        l += [i for i in self.items if i.frequency == new_node.frequency and i.item != '*']
        l += [new_node]
        l += [i for i in self.items if i.frequency == new_node.frequency and i.item == '*']
        l += [i for i in self.items if i.frequency < new_node.frequency]
        self.items = l

    def preorder(self, node,level=0):
        if node:
            self.preorder(node.right, level+1)
            print('','     '*level + node.item)
            self.preorder(node.left, level+1)

    def huffman_code(self, node, bit=''):
        d = dict()
        if node.item != '*':
            return {node.item: bit}
        d.update(self.huffman_code(node.right, bit+'1'))
        d.update(self.huffman_code(node.left, bit+'0'))
        return d

token = [i for i in input('Enter Input : ')]
t = Huffman()
t.prepare(token)
while len(t.items) > 1:
    t.insert()
t.root = t.items[0]
d = t.huffman_code(t.root)
print(d)
t.preorder(t.root,0)
print('',end='')
print('Encoded! :',''.join(d[i] for i in token))