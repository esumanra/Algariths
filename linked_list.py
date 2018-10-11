class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class Linked_List:

    def __init__(self):
        self.head = None


    def insert(self, data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head

            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode

            currentNode.nextNode = newNode

    def remove(self, data):

        if self.head is None:
            print("List is empty")

        curr = self.head
        prev = None

        while curr.data != data:
            prev = curr
            curr = curr.nextNode

        if prev is None:
            self.head = curr.nextNode
        else:
            prev.nextNode = curr.nextNode

    def traverse(self):

        currentNode = self.head
        llist = ''
        while currentNode is not None:
            llist += str(currentNode.data) + ' --> '
            currentNode = currentNode.nextNode

        print(llist.strip(' --> '))

    def reverse_linked_list(self):
        current = self.head
        prev = None
        next = None

        while current is not None:
            next = current.nextNode
            current.nextNode = prev
            prev = current
            current = next

        self.head = prev

# ll = Linked_List()
# #inserting
# for k in range(1, 11):
#     ll.insert(k)
# ll.traverse()
# ll.remove(9)
# ll.traverse()