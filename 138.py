# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node_map = {}
        rev_map = {}
        cur = head
        new_head = None
        last_node = None
        while cur:
            if cur.random is not None:
                node_map[cur.label] = cur.random.label
            new_node = RandomListNode(cur.label)
            rev_map[cur.label] = new_node

            if new_head is None:
                new_head = new_node
                last_node = new_node
            else:
                last_node.next = new_node
                last_node = new_node
            cur = cur.next

        for k in node_map:
            rev_map[k].random = rev_map[node_map[k]]

        return new_head