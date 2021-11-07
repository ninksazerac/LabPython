'''
พ่อจ๋าอยู่ไหน
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
และให้หา พ่อ(father node) ของ node ที่กำหนด
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)

        else:
            current = self.root
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


def father(r, data):
    t_tree = r;
    while True:
        if (t_tree.data > data and t_tree.left != None):
            # print("in 1")
            if (t_tree.left.data == data):
                print(t_tree.data)
                break;

            else:
                # print("finnish 1")
                t_tree = t_tree.left


        elif (t_tree.data < data and t_tree.right != None):
            # print("in 2")
            if (t_tree.right.data == data):
                print(t_tree.data)
                break;

            else:
                # print("finnish 2")
                t_tree = t_tree.right

        elif (t_tree.data == data):
            print("None Because", data, "is Root")
            break;

        else:
            print("Not Found Data")
            break;


tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)

printTree90(tree.root)
father(tree.root, data[1])