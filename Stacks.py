class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        self.items.pop()

    def checks(self):
        self.items

    def addfront(self, element):

        self.items.append(element)

    def addrear(self, element):

        self.items.insert(0, element)

newStack = Stack()
newStack.push(1)
print(newStack)

