class Queue:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.items.pop(0)  # slow: must move all other element to 0 index

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'Queue contains {self.items}'