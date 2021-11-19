'''
Closest Value
จงเขียนฟังก์ชั่นสำหรับการ insert แบบ Binary Search Tree (BST) โดยที่ input ตัวแรกจะเป็น root เสมอและจงเขียนฟังก์ชั่นสำหรับการหาค่าที่ใกล้เคียง input ที่รับเข้ามาที่สุดที่อยู่ใน BST ที่ทำการ insert ครบแล้ว

รูปแบบการรับ input จะแบ่งโดย '/'

1.ชุดของ BST ที่จะทำการ insert โดยตัวแรกจะเป็น root เสมอ
2.ค่าที่จะนำมาเปรียบเทียบกับค่าใน BST ที่ทำการ insert แล้ว

รูปแบบ output

จะ printTree ทุกครั้งที่มีการ insert ค่าเข้าและเมื่อทำการ insert จบจะเรียกใช้ฟังก์ชั่น closestValue(root,value) และแสดงค่าที่ใกล้เคียงที่สุดจาก BST
*** ถ้าหากค่าที่รับเข้ามาเทียบมีอยู่ใน BST ให้ return ค่านั้นออกมาได้เลย และหากมีค่าที่อยู่ใกล้มากกว่า 1 จำนวนให้แสดงจำนวนที่มากที่สุดที่อยู่ใกล้ค่านั้น ***
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.lst = []

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while currentNode is not None:
                if data > currentNode.data:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        break
                    currentNode = currentNode.right
                elif data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    currentNode = currentNode.left
        return self.root

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        self.lst.append(node.data)
        self.inOrder(node.right)


def closestValue(rootNode, value):
    cValue = None
    tree.inOrder(rootNode)
    for i in tree.lst:
        cValue = i
        if i == value or i > value:
            break

    print('Closest value of', value, ':', cValue)
inp, k = input('Enter Input : ').split('/')

k = int(k)
inp = [int(i) for i in inp.split()]

tree = BinarySearchTree()

for i in inp:
    root = tree.insert(i)
    tree.printTree(root)
    print('--------------------------------------------------')

closestValue(root, k)