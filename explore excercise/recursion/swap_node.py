# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:

            pointer1 = head
            pointer2 = head.next
            pointer1.next = pointer2.next
            pointer2.next = pointer1
            head = pointer2

            while pointer1.next != None and pointer1.next.next != None:
                pointer2 = pointer1.next
                pointer1.next = pointer1.next.next
                pointer2.next = pointer1.next.next
                pointer1.next.next = pointer2
                pointer2 = pointer1.next
                pointer1 = pointer2.next

            return head
