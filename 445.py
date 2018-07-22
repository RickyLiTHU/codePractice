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
        s = self.convert(l1) + self.convert(l2)
        return self.toLinkedList(s)
    
    def convert(self,l):
        s = ""
        p = l
        while p != None:
            s += str(p.val)
            p = p.next
        return int(s)
    
    def toLinkedList(self,s):
        p = ListNode(0)
        h = p
        arr = list(str(s))
        for c in arr:
            node = ListNode(int(c))
            p.next = node
            p = p.next
        return h.next