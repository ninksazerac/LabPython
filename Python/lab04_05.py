#color cruch 2
class Queue:
    def __init__(self) -> None:
        self.data = []

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

    def __str__(self):
        res = ''
        for i in self.data:
            res += i
        return res

    def Bastr(self):
        res = ''
        for i in self.data:
            res = i + res
        return res


mirItem = Queue()
normQ = Queue()
mirrQ = Queue()
Run = True
Interrupt = False
norm, mirr = input('Enter Input (Normal, Mirror) : ').split()
norm = list(norm)
mirr = list(mirr)
normS = len(norm)
mirrS = len(mirr)
mirrC = 0
normC = 0
failedC = 0

while mirrS > 2 and Run == True:
    for i in range(mirrS - 1, -1, -1):
        if mirr[i] == mirr[i - 1] == mirr[i - 2]:
            mirItem.enqueue(mirr[i])
            mirr.pop(i - 2)
            mirr.pop(i - 2)
            mirr.pop(i - 2)
            mirrS -= 3
            mirrC += 1
            break
        if i == 0:
            Run = False
Run = True

while normS > 2 and Run == True:
    for i in range(0, normS - 2):
        if norm[i] == norm[i + 1] == norm[i + 2]:
            if mirItem.size() > 0:
                norm.insert(i + 2, mirItem.dequeue())
                normS += 1
                Interrupt = True
            if norm[i] == norm[i + 1] == norm[i + 2]:
                norm.pop(i)
                norm.pop(i)
                norm.pop(i)
                normS -= 3
                if Interrupt == True:
                    failedC += 1
                else:
                    normC += 1
            Interrupt = False
            break
        if i == normS - 3:
            Run = False

if normS > 0:
    for i in norm:
        normQ.enqueue(i)
if mirrS > 0:
    for i in mirr:
        mirrQ.enqueue(i)

print('NORMAL :')
print(normS)
print(normQ.Bastr() if normS > 0 else 'Empty')
print(normC, 'Explosive(s) ! ! ! (NORMAL)')
if failedC > 0:
    print('Failed Interrupted', failedC, 'Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(mirrS)
print(mirrQ if mirrS > 0 else 'ytpmE')
print('(RORRIM) ! ! ! (s)evisolpxE', mirrC)