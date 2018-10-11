from linked_list_util import Node, create_list, traverse

def remove_duplicates_unsorted_l_list(head):
    prev = None
    unique = set()
    while head:
        if head.data in unique:
            prev.nextNode = head.nextNode
        else:
            unique.add(head.data)
            prev = head
        head = head.nextNode

# another implementation
def remove_dup(h):
    cur = h
    prev = None
    unique = set()

    while cur is not None:

        if cur.data not in unique:
            unique.add(cur.data)
            prev = cur
        else:
            prev.nextNode = cur.nextNode

        cur = cur.nextNode
    return cur

s_list = "aabbbcdde"
h = create_list(s_list[::-1])
# traverse(h)
remove_duplicates_unsorted_l_list(h)
traverse(h)