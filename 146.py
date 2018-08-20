class LinkList:
    def __init__(self, value):
        self.value = value
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = None
        self.tail = self.head
        self.hash_table = {}
        self.capacity = capacity
        self.current_capacity = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #print "get",key
        if key in self.hash_table:
            value, pointer = self.hash_table[key]
            if pointer != self.tail:
                self.tail.next = LinkList(key)
                self.tail = self.tail.next
                next_node = pointer.next
                if next_node is not None:
                    pointer.next = next_node.next
                    pointer.value = next_node.value
                    self.hash_table[next_node.value][1] = pointer
                self.hash_table[key][1] = self.tail
            #self.printLinkList(self.head)
            return value
        else:
            return -1
    def printLinkList(self, t):
        while t:
            print t.value,
            t = t.next
        print ""
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        #print "put",key,value
        if key in self.hash_table:
            self.get(key)
            self.hash_table[key] = [value,self.tail]
            return
        if self.current_capacity == 0:
            self.head = LinkList(key)
            self.tail = self.head
            self.current_capacity += 1
            
        elif self.current_capacity < self.capacity:
            self.tail.next = LinkList(key)
            self.tail = self.tail.next
            self.current_capacity += 1
        else:
            #print self.head.value
            del self.hash_table[self.head.value]
            self.head = self.head.next
            self.tail.next = LinkList(key)
            self.tail = self.tail.next
        #print self.hash_table
        #self.printLinkList(self.head)
        self.hash_table[key] = [value,self.tail]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)