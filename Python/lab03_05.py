#แปลงเลขฐาน 10 เป็น เลขฐาน 2 ด้วย STACK
class Stack():
    def __init__(self):
        self.stack = []

    def __str__(self):
        if self.is_empty():
            return "Empty"
        s = ""
        for i in self.stack:
            s += str(i) + " "
        return s

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else "Empty"

    def peek(self):
        return self.stack[-1] if not self.is_empty() else "Empty"

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)

    def clear(self):
        return self.stack.clear()


def dec2bin(dec_num):
    s = Stack()
    while dec_num > 0:
        temp = dec_num % 2
        s.push(temp)
        dec_num = dec_num // 2
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num


if __name__ == '__main__':
    print(" ***Decimal to Binary use Stack***")
    token = input("Enter decimal number : ")
    print("Binary number : ", end='')
    print(dec2bin(int(token)))