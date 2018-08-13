class Trie(object):
    
    class Node(object):
    
        def __init__(self, val):
            self.val = val
            self.children = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tries = {}
        self.words = set()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.tries.get(word[0], Trie.Node(word[0]))
        head = node
        for c in word[1:]:
            if c not in node.children:
                node.children[c] = Trie.Node(c)
            node = node.children[c]
        if head not in self.tries:
            self.tries[word[0]] = head
        self.words.add(word)
            

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.words

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix[0] not in self.tries: return False
        node = self.tries[prefix[0]]
        for c in prefix[1:]:
            if c not in node.children: return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)