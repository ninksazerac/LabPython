#infix to postfix
class Stack():
    def __init__(self):
        self.stack = []
    def __str__(self):
        if self.is_empty:
            return "Empty"
        s = ""
        for i in self.stack:
            s += str(i) + " "
        return s
    def pop(self):
        return self.stack.pop() if not self.is_empty() else "Empty"
    def push(self, items):
        return self.stack.append(items)
    def peek(self):
        return self.stack[-1] if not self.is_empty() else "Empty"
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self.stack)
    def clear(self):
        return self.stack.clear()

def infix2postfix() :
    print(" ***Infix to Postfix***")
    inp = list(input("Enter Infix expression : "))
    sstack = Stack()
    priority = { "+":1, "-":1, "*":2, "/":2, "^":3, "(":3 }
    print("PostFix : ")
    for a in inp:
        if a in "+-*/^(":
            if not sstack.is_empty() and priority.get(a) <= priority.get(sstack.peek()):
                while not sstack.is_empty() and sstack.peek() != "(" and priority[a] <= priority[sstack.peek()]:
                    print(sstack.pop(), end= "")
            sstack.push(a)
        elif a == ")":
            while not sstack.is_empty() and sstack.peek() != "(":
                print(sstack.pop(), end = "")
            sstack.pop()
        else: print(a, end= "")
    while sstack.size() != 0:
        print(sstack.pop(), end= "")

if __name__ == "__main__":
   infix2postfix()
