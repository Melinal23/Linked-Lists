class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def removeNthFromEnd(head, n):

    if not head:
        return None

    length = get_list_length(head)

    if length == 1 and n != 1:
        return head

    if length == 1 and n == 1:
        return None

    index = length - n

    if index == 0:
        return head.next

    reftohead = head

    prev = None
    numofnodesseen = 0

    while head:
        if numofnodesseen == index:
            prev.next = head.next
            break
        prev = head
        head = head.next
        numofnodesseen += 1

    if (numofnodesseen == index):
        prev

    return reftohead


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    length  = get_list_length(head)
    first = head

    length -= n

    first = dummy

    while (length > 0):
        length -= 1
        first = first.next

    first.next = first.next.next

    return dummy.next

def get_list_length(list):
    if not list:
        return 0

    return get_list_length(list.next) + 1