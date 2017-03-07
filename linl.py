class Node(object):
    def __init__(self, datax):
        self.next_node = None
        self.data = datax

n1 = Node(1)

n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next_node = n2
n2.next_node = n3
n3.next_node = n4

temp_node = None
curr_node = start_node = Node(1)

for i in range(1, 11):
    if i > 1:
        temp_node = curr_node
        temp_node.next_node = Node(i)
        curr_node = temp_node.next_node


print(" The node: are")

while  start_node:
    print("Node data {0}".format(start_node.data))
    start_node = start_node.next_node









