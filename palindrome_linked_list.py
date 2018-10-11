class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def make_linked_list(st):
    head = None
    for item in st:
        newNode = Node(item)

        if head is None:
            head = newNode
        else:
            newNode.next = head
            head = newNode
    return head


def compare_two_lists(first, second):
    while second is not None:
        if first.data != second.data:
            return False

        first = first.next
        second = second.next
    return True


def traverse(head):
    currNode = head
    while currNode is not None:
        print(currNode.data),
        currNode = currNode.next


def reverseList(head):
    prev = next_node = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev  # coz prev will be new head - end of list


def is_linked_list_palindrome(head):
    fast = slow = head
    mid = None

    # find mid of linked list
    while True:
        fast = fast.next.next
        if fast is None:
            mid = slow.next
            break
        elif fast.next is None:
            mid = slow.next.next
            break

        slow = slow.next
    print("\nmiddle ele:{}".format(mid.data))

    # reverse the second half
    second_head = reverseList(mid)

    # compare two lists
    if compare_two_lists(head, second_head):
        print("linked list is palindrom")
    else:
        print("Not a palindrome linked list")

    # reverse the second list
    reverseList(second_head)


s = "mani"
head = make_linked_list(s)
head = reverseList(head)
traverse(head)
is_linked_list_palindrome(head)
traverse(head)
