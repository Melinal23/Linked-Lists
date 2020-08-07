class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):     #exceeds time limit!
    # edge cases
    if not head:
        return []
    if head.next == None:
        return [head.val]

    temp = []

    curr = head
    while (curr != None):  # put all linked list val in an array
        temp.append(curr.val)
        curr = curr.next

    answer = [0] * len(temp)

    for i in range(len(temp)):  # loop through linked list vals and find next larger
        curr_val = temp[i]
        next_large = 0
        for j in range(i, len(temp)):
            if temp[j] > curr_val:
                next_large = temp[j]
                break
        if next_large:
            answer[i] = next_large

    return answer

def nextLargerNodes_student_soln(head):
    #edge cases
    if not head:
        return []
    if head.next == None:
        return [0]

    temp = []

    curr = head
    while(curr):      #put all linked list val in an array
        temp.append(curr.val)
        curr = curr.next

    answer = [0] * len(temp)
    stack = []
    for i in range(len(temp)): #loop through linked list vals and find next larger
        # pop greater elements off the stack and add them to ans.
        while stack != [] and temp[stack[-1]] < temp[i]:
            answer[stack.pop()] = temp[i]
        # Add smaller elments  to the top of the stack.
        stack.append(i)

    return answer