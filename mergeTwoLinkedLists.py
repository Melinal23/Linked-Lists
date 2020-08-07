class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if not l1 and not l2:
        return None
    elif not l1:
        return l2
    elif not l2:
        return l1

    if (l1.val < l2.val):
        newlist = l1
        finallist = newlist
        l1 = l1.next
        while (l1 and l2):
            if (l1.val < l2.val):
                newlist.next = l1
                newlist = newlist.next
                l1 = l1.next
            elif (l2.val < l1.val):
                newlist.next = l2
                newlist = newlist.next
                l2 = l2.next
            else:
                newlist.next = l1
                newlist = newlist.next
                l1 = l1.next

        if (not l1):
            newlist.next = l2
        if (not l2):
            newlist.next = l1
    elif (l2.val < l1.val):
        newlist = l2
        finallist = newlist
        l2 = l2.next
        while (l1 and l2):
            if (l1.val < l2.val):
                newlist.next = l1
                newlist = newlist.next
                l1 = l1.next
            elif (l2.val < l1.val):
                newlist.next = l2
                newlist = newlist.next
                l2 = l2.next
            else:
                newlist.next = l1
                newlist = newlist.next
                l1 = l1.next

        if (not l1):
            newlist.next = l2
        if (not l2):
            newlist.next = l1
    else:
        newlist = l1
        finallist = newlist
        l1 = l1.next
        while (l1 and l2):
            if (l1.val < l2.val):
                newlist.next = l1
                newlist = newlist.next
                l1 = l1.next
            elif (l2.val < l1.val):
                newlist.next = l2
                newlist = newlist.next
                l2 = l2.next
            else:
                newlist.next = l1
                newlist = newlist.next
                l1 = l1.next

        if (not l1):
            newlist.next = l2
        if (not l2):
            newlist.next = l1

    return finallist

"""This is the exact same soln as above but with a dummy head implementation, notice the code size difference"""
# def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#
#     if not l1 and not l2:
#         return None
#     elif not l1:
#         return l2
#     elif not l2:
#         return l1
#
#     newlist = ListNode(None)
#     finallist = newlist
#
#     while (l1 and l2):
#         if (l1.val < l2.val):
#             newlist.next = l1
#             l1 = l1.next
#         else:
#             newlist.next = l2
#             l2 = l2.next
#         newlist = newlist.next
#
#     if (not l1):
#         newlist.next = l2
#     if (not l2):
#         newlist.next = l1
#
#     return finallist.next  # excluding the dummyhead

def mergeTwoLists_student_soln(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val > l2.val:
        l_start = ListNode(val=l2.val)
        l2 = l2.next
    else:
        l_start = ListNode(val=l1.val)
        l1 = l1.next

    l = l_start
    while l1 is not None or l2 is not None:
        if l1 is None:
            l.next = l2
            break
        elif l2 is None:
            l.next = l1
            break

        if l1.val > l2.val:
            l.next = ListNode(val=l2.val)
            l2 = l2.next
        else:
            l.next = ListNode(val=l1.val)
            l1 = l1.next
        l = l.next

    return l_start

def mergeTwoLists_codepath_soln(l1, l2):
    return_head = ListNode(-1)
    dummy_head = return_head
    while l1 and l2:
        if l1.val < l2.val:
            dummy_head.next = ListNode(l1.val)
            l1 = l1.next
        else:
            dummy_head.next = ListNode(l2.val)
            l2 = l2.next
        dummy_head = dummy_head.next
    leftover = l1 if l1 else l2
    while leftover:
        dummy_head.next = ListNode(leftover.val)
        leftover = leftover.next
        dummy_head = dummy_head.next
    return return_head.next