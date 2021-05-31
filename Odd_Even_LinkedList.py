class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    odd = ListNode(None)
    oddtail = odd
    even = ListNode(None)
    eventail = even
    temp = head
    index = 1

    while (temp):
        if (index % 2 == 1):  # odd
            oddtail.next = temp
            oddtail = oddtail.next
        else:  # even
            eventail.next = temp
            eventail = eventail.next

        temp = temp.next
        index += 1

    eventail.next = None
    oddtail.next = even.next

    return odd.next

def oddEvenList_LeetCodeSoln(head):
    if not head:
        return None

    odd = head
    even = head.next
    evenHead = even

    while(even and even.next):
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = evenHead

    return head