# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def list_to_number(l):
            result = 0
            counter = 0
            while l is not None:
                result += l.val * 10 ** counter
                l = l.next
                counter += 1
            return result

        def number_to_list(n):
            if len(str(n)) == 1:
                return ListNode(n)
            else:
                header = ListNode(n%10)
                pointer = header
                n = n//10
                while len(str(n)) > 1:
                    pointer.next = ListNode(n%10)
                    pointer = pointer.next
                    n = n//10
                pointer.next = ListNode(n)
                return header

        return number_to_list(list_to_number(l1) + list_to_number(l2))


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
list_to_number(l1)
list_to_number(l2)
a = number_to_list(324)
a = number_to_list(0)

l1 = ListNode(0)
l2 = ListNode(0)

Solution().addTwoNumbers(l1, l2)