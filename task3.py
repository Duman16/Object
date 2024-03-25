class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print("ok")

    def pop(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items.pop())

    def back(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[-1])

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []
        print("ok")

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()

while True:
    command = input().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        stack.pop()
    elif command[0] == "back":
        stack.back()
    elif command[0] == "size":
        stack.size()
    elif command[0] == "clear":
        stack.clear()
    elif command[0] == "exit":
        print("bye")
        break
