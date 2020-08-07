class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseList(head):
    if not head:
        return None

    rev = ListNode(head.val)
    prev = None
    ptr = head.next

    while (ptr):
        prev = rev
        curr = ListNode(ptr.val)
        curr.next = prev
        rev = curr
        ptr = ptr.next

    return rev

def reverseList_leetcode_soln(head):
    prev = None
    curr = head
    while (curr != None):
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp

    return prev