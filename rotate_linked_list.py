class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        list_len = get_length(head)

        temp = head

        while (temp.next):
            temp = temp.next

        temp.next = head  # make cyclic

        k = k % list_len
        move = list_len - k
        newHead = head
        prev = None
        while (move > 0):
            prev = newHead
            newHead = newHead.next
            move -= 1

        prev.next = None

        return newHead


def get_length(head):
    if not head:
        return 0

    return get_length(head.next) + 1