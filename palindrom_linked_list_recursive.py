import linked_list_util as l

s = "radar"
h = l.create_list(s[::-1])

def is_palindrome_util(right, left):
    if right is None:
        return True

    x = is_palindrome_util(right.nextNode, left)
    if not x:
        return False

    y = False
    if left.data == right.data:
        y = True
    left = left.nextNode

    return y

def is_palindrome(head_node):
    if is_palindrome_util(head_node, head_node):
        print("Palindrome")
    else:
        print("Nope")

def recursive_print(head):
    cur = head

    if not cur:
        return

    recursive_print(cur.nextNode)
    print(cur.data)


recursive_print(h)
is_palindrome(h)