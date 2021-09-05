#Postfix Calculator
class Stack:

    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        if len(self.item) > 0:
            return self.item.pop()
        else:
            print('list is empty')

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return len(self.item) == 0

    def dequeue(self):
        if len(self.item) > 0:
            return self.item.pop(0)
        else:
            print('list is empty')

print(' ***Postfix expression calcuation***')
s = Stack()
Inp = input('Enter Postfix expression : ').split()

for i in Inp:
    if i in ('+','-','*','/'):
        Operand1, Operand2 = s.pop(),s.pop()
        if i == '-':
            s.push(Operand2-Operand1)
        elif i == '+':
            s.push(Operand2+Operand1)
        elif i == '*':
            s.push(Operand2*Operand1)
        elif i == '/':
            s.push(Operand2/Operand1)
    else:
        s.push(int(i))

if not s.isEmpty():
    print('Answer : ','{:.2f}'.format(s.pop()))
else:
    print('Empty list , cannot fucking pop.')