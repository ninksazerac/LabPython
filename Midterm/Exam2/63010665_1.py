class Stack:

    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def is_Empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[-1]

    def bottom(self):
        return self.item[0]

    def __str__(self):
        show = list(map(str, self.item))
        show = " ".join(show)
        return f"Data in Stack is : {show}"


s1 = Stack()
Choice = int(input("Enter choice : "))
if Choice == 1:
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :", s1.peek())
    print("Bottom of stack :", s1.bottom())
elif Choice == 2:
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :", s1.is_Empty())
elif Choice == 3:
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :", s1.size())
