# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return []
        elif head.next == None:
            return head
        cur = head
        nex = cur.next
        while nex.next != None:
            temp = nex.next
            nex.next = cur
            cur = nex
            nex = temp
        nex.next = cur
        head.next = None
        return nex