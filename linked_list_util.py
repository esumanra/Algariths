class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

def push(head, data):
    newNode = Node(data)
    newNode.nextNode = head
    head = newNode
    return head

def traverse(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.nextNode

def create_list(l_str):
    head = Node(l_str[0])
    for l in l_str[1:]:
        head = push(head, l)
    return head