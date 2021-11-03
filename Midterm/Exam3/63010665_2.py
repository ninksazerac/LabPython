'''
2 - Exam_3_2_2a
จงเขียนโปรแกรมแบบ Recursive เพื่อหาค่า Min ของ Input ที่ป้อนมา แล้วแสดงผลดังตัวอย่าง
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right
        return self.root

    def min(self):
        if self.root is None:
            return
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data


T = BST()
arr = [int(e) for e in input('Enter Input : ').split()]
for e in arr:
    root = T.create(e)
print("Min :",T.min())