# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


### Iteration
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = None
        while head != None:
            tmp = ListNode(head.val)
            tmp.next = result
            result = tmp
            head = head.next
        return result

### recursion
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None or head == None:
            return head
        else:
            p = ListNode(head)
            head.next.next = head

            p.next = reverseList(head.next)


        return p
