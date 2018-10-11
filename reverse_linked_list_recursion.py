from linked_list_util import create_list, Node, traverse

count = None


def reverse_linked_list_recursion(p):
    if p.nextNode == None:
        global head
        global count
        head = p
        count = 1
        return True

    reverse_linked_list_recursion(p.nextNode)
    p.nextNode.nextNode = p
    p.nextNode = None
    count += 1
    return head


s_list = "123"
h = create_list(s_list[::-1])
traverse(h)
r_h = reverse_linked_list_recursion(h)
traverse(r_h)
print("count :%s" % count)
