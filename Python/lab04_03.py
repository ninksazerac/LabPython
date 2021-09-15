#ร้านหนังสือ
class Queue :
    def __init__(self) -> None:
        self.data = []

    def __str__(self) -> str:
        return str(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def enqueue(self, new_data):
        return self.data.append(new_data)

    def dequeue(self):
        if self.is_empty():
            return 'Empty'
        return self.data.pop(0)

    def size(self):
        return len(self.data)

Q = Queue()
x = input('Enter Input : ').split('/')
book = x[0].split()
oper = x[1].split(',')
for i in range(0,len(book)):
    Q.enqueue(book[i])
for i in range(0,len(oper)):
    x = oper[i].split()
    if x[0] == 'E':
        Q.enqueue(x[1])
    elif x[0] == 'D':
        Q.dequeue()
if len(Q.data) == len(set(Q.data)):
    print('NO Duplicate')
else :
    print('Duplicate')