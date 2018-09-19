# Definition for singly-linked list.
#   class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l = ListNode(0)
        carry = 0
        while l1 or l2:
            num = carry
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            l.next = ListNode(num%10)
            l = l.next
            carry = num//10
        if carry == 1:
            l.next = ListNode(1)

        return head.next
