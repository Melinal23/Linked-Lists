class ListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def getIntersectionNode(headA, headB):

    if not headA or not headB:  # If one of the linked lists are None
        return None  # then there is no intersection

    headA_len = get_len(headA)
    headB_len = get_len(headB)

    if headA_len > headB_len:
        headA = make_same_length(headA, headA_len, headB_len)
    elif headB_len > headA_len:
        headB = make_same_length(headB, headB_len, headA_len)

    while (headA and headB and (headA != headB)):
        headA = headA.next
        headB = headB.next

    return headA  # can return headB as well, both point to the same node ref.


def get_len(head):
    if not head:
        return 0

    return get_len(head.next) + 1


def make_same_length(head, len1, len2):
    while (len1 > len2):
        head = head.next
        len1 -= 1

    return head
