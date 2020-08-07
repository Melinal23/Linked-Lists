#Time complexity: O(n) Space Comp.: O(1)
def hasCycle(head):
    if not head or not head.next:
        return False

    sp = head
    fp = head.next
    while fp and fp.next:
        if fp == sp or fp.next == sp:
            return True
        fp = fp.next.next
        sp = sp.next
    return False

def hasCycle_student_soln(head):
    slow = head
    fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            return True
    return False