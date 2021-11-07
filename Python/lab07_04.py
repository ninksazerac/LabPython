'''
delete node in tree

ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
โดยมีการป้อน input ดังนี้
i <int> = insert data
d <int> = delete data
หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

treedata = []
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    # print('less than', val, '<', current.data)
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    # print('greater than', val, '>', current.data)
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    def delete(self, r, data):
        if r is None:  # base case
            print("Error! Not Found DATA")
            return
        if r.data != data:  # not found

            if r.data > data:
                r.left = self.delete(r.left, data)  # not found left
            elif r.data < data:
                r.right = self.delete(r.right, data)  # not found right



        else:  # found !!!!

            if r.left is None:  # left None
                node = r.right
                return node
            elif r.right is None:  # right None
                node = r.left
                return node
            else:
                current = r.right
                while current.left is not None:
                    current = current.left

                r.data = current.data  # replace delete
                r.right = self.delete(r.right, current.data)  # permanent delete recursive.....

        return r



def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in range(len(data)):
    data[i] = data[i].split()
    if data[i][0] == 'd':
        print("delete " + (data[i][1]))
        tree.root = tree.delete(tree.root, int(data[i][1]))
        printTree90(tree.root)
    elif data[i][0] == 'i':
        print("insert " + (data[i][1]))
        tree.insert(int(data[i][1]))
        printTree90(tree.root)