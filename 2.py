# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        dummy = l3
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            sum = carry
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            carry = int (sum / 10)
            l3.next = ListNode(sum % 10)
            l3 = l3.next
        return dummy.next