def main():
    word = "A"

def find_pal(word):

    # base case
    if word == "" or len(word) == 1:
        return True

    if word[0] == word[-1]:  # if the first letter and the last are equal check the substring
        return find_pal(word[1:-1])
    else:  # if they are not equal it is not a palindrome
        return False

# this is the better solution because the rec solution has greater space requirements d
# due to the func calls on the stack
# also word[1:-1] creates a new string from scratch so it takes more time
def find_pal_itr(word):

    start = 0
    end = len(word) - 1

    # this is O(n) because we iterate through the word
    # space complexity is O(1)
    while (start < end):
        if(word[start] != word[end]):
            return False
        start += 1
        end -= 1

    return True

def reverse_string(word):

    temp = ""

    # this is O(n), n being the length of the string, bec it
    # creates a new string
    return word[::-1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome_linked_list (Node):
    if Node is None or Node.next is None:
        return True
    else:
        curr = Node
        stack = []
        while (curr != None):
            stack.append(curr.data)
            curr = curr.next

        temp = Node
        while (temp != None):
            val = stack.pop()
            if(val != temp.data):
                return False
            temp = temp.next

    return True


# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
# Input: 1->2
# Output: false
#
# Example 2:
# Input: 1->2->2->1
# Output: true


def isPalindrome(node):
    if not node:
        return False

    fullLength = getLength(node)

    if fullLength == 1:
        return True

    firstHalf = []

    currentNode = 0

    while (currentNode < (fullLength / 2)):
        firstHalf.append(node.data)
        node = node.next
        currentNode += 1

    if fullLength % 2 == 1:
        firstHalf.pop()

    if len(firstHalf) == 1:
        currentNode = 0

    while (currentNode >= 0 and node):
        if (node.data != firstHalf[currentNode]):
            return False
        node = node.next
        currentNode -= 1

    if (currentNode > 0):
        return False

    return True


def getLength(node):
    length = 0
    while (node != None):
        length += 1

        if (node.next == None):
            return length
        node = node.next
    return length


def isPalindrome(head) :
    dummy = head
    list_length = listLength(dummy)
    l1, l2 = head, head
    for _ in range(list_length // 2):
        l2 = l2.next

    rev_l2 = reverse_list(l2)

    while l1 and rev_l2:
        if l1.val != rev_l2.val:
            return False
        l1, rev_l2 = l1.next, rev_l2.next
    return True


def listLength(head):
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


if __name__ == '__main__':
    main()
