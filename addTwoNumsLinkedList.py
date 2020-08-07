class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    elif not l1 and not l2:
        return None

    dummyNode = ListNode(None)
    reftodummy = dummyNode
    carry = 0

    while (l1 and l2):
        dummyNode.next = ListNode((l1.val + l2.val + carry) % 10)

        carry = (l1.val + l2.val + carry) // 10

        dummyNode = dummyNode.next
        l1 = l1.next
        l2 = l2.next

    if l1 and not l2:
        while (l1):
            dummyNode.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            dummyNode = dummyNode.next
    if l2 and not l1:
        while (l2):
            dummyNode.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            dummyNode = dummyNode.next

    if carry:
        dummyNode.next = ListNode(1)

    return reftodummy.next