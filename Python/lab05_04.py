#VIM Text Editor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.nodeAt(self.size()-1), str(self.nodeAt(self.size()-1).value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None :
            self.head = Node(item)
        else :
            self.insert(self.size(),item)

    def addHead(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            self.insert(0,item)
    def nodeAt(self,i) :
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def insert(self, pos, item):
        if self.head == None:
            self.head = Node(item)
        elif pos >= 0:
            if pos == 0:
                x = Node(item)
                x.next = self.nodeAt(0)
                self.head = x
                x.next.previous = x
            elif pos == self.size():
                x = Node(item)
                p = self.nodeAt(self.size()-1)
                p.next = x
                x.previous = p
            elif pos < self.size():
                p = self.nodeAt(pos).previous
                q = self.nodeAt(pos)
                x = Node(item)
                p.next = x
                q.previous = x
                x.next = q
                x.previous = p
            else:
                self.insert(self.size(),item)
        else:
            if abs(pos)<=self.size():
                self.insert(self.size()+pos,item)
            elif True:
                self.insert(0,item)

    def search(self, item):
        if self.isEmpty():
            return 'Not Found'
        buffer = self.nodeAt(0)
        for i in range(0,self.size()):
            if str(buffer.value) == str(item):
                return 'Found'
            buffer = buffer.next
        return 'Not Found'

    def index(self, item):
        buffer = self.head
        count = 0
        while buffer is not None:
            if buffer.value == item:
                return count
            count += 1
            buffer = buffer.next
        return -1

    def size(self):
        buffer = self.head
        count = 0
        while buffer is not None:
            count += 1
            buffer = buffer.next
        return count

    def pop(self, pos):
        if self.size() == 1 and pos == 0:
            self.head = None
            return 'Success'
        elif pos == 0:
            x = self.nodeAt(1)
            self.head = x
        elif self.size() == 0:
            return 'Out of Range'
        elif pos < 0 and abs(pos)>self.size()-1:
            return 'Out of Range'
        elif pos < 0:
            self.pop(self.size()-1+pos)
        elif pos > self.size()-1:
            return 'Out of Range'
        elif pos == self.size()-1 and self.size()>1:
            x = self.nodeAt(self.size()-2)
            x.next = None
            return 'Success'
        else:
            x = self.nodeAt(pos)
            p = self.nodeAt(pos-1)
            q = self.nodeAt(pos+1)
            p.next = q
            q.previous = p
            return 'Success'

L = LinkedList()
inp = input('Enter Input : ').split(',')
cur = 0
for i in inp:
    if i[0] == 'I':
        L.insert(cur,i[2:])
        cur += 1
    if i[0] == 'L' and cur > 0:
        cur -= 1
    if i[0] == 'R' and cur < L.size():
        cur += 1
    if i[0] == 'B' and cur > 0:
        L.pop(cur-1)
        cur -= 1
    if i[0] == 'D' and cur < L.size():
        L.pop(cur)
L.insert(cur,'|')
print(L)