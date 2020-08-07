class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    before = ListNode(-1)
    before_head = before
    after = ListNode(-1)
    after_head = after

    curr = head
    while (curr):  # while we are not at the end of the list
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next

    after.next = None
    before.next = after_head.next  # exclude dummy node

    return before_head.next  # exclude the dummy node
