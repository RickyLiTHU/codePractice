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
        _head = head
        
        while True:
            if head == None: break
            head = head.next 
            if _head == None or _head.next == None: break
            _head = _head.next.next
            if head == _head: return True
        
        return False