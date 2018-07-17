# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        quick = slow = head
        
        while True:
            try:
                quick = quick.next.next
            except:
                return None
            slow = slow.next
            if quick == slow: break
        while head != slow:
            head = head.next
            slow = slow.next
            
        return slow