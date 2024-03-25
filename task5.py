class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print("ok")

    def pop(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items.pop(0))

    def front(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[0])

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []
        print("ok")

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()

while True:
    command = input().split()
    if command[0] == "push":
        queue.push(int(command[1]))
    elif command[0] == "pop":
        queue.pop()
    elif command[0] == "front":
        queue.front()
    elif command[0] == "size":
        queue.size()
    elif command[0] == "clear":
        queue.clear()
    elif command[0] == "exit":
        print("bye")
        break
