'''
4 - BST Height
เขียน Binary Search Tree
แล้วรับ input แสดงผล ตามตัวอย่าง
ห้ามแก้ไขในส่วนของ main program ด้านล่าง

class Node:
    .................

class BinarySearchTree:
   ......................

def height(obj):
   .......................

print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
arr = list(map(int, input("Enter Input : ").split()))
for e in arr:
    tree.create(e)
print("Height = ",height(tree.root),end="\n\n")
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
    def create(self, inp):
        if self.root is None:
            self.root = Node(inp)
        else:
            curr = self.root
            while True:
                if inp < curr.data:
                    if curr.left is None:
                        curr.left = Node(inp)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(inp)
                        break
                    curr = curr.right
        return self.root
def height(obj):
    if not obj:
        return -1
    a = height(obj.left) + 1
    b = height(obj.right) + 1

    return max(a, b)



print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
arr = list(map(int, input("Enter Input : ").split()))

for e in arr:

    tree.create(e)

print("Height = ",height(tree.root),end="\n\n")