from collections import defaultdict
import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        words = set(wordList)
        if endWord not in words:
            return []
        words.remove(endWord)
        if beginWord in words:
            words.remove(beginWord)
        set1, set2 = set([beginWord]), set([endWord])
        pre1, pre2 = defaultdict(list), defaultdict(list)
        pre1[beginWord+'#'] = True
        pre2[endWord+'#'] = True
        midpoints = set()
        while set1:
            tmp = set()
            for w in set1:
                for i in range(len(w)):
                    for c in string.ascii_lowercase:
                        if w[i] == c:
                            continue
                        new_word = w[:i] + c + w[i+1:]
                        if new_word in set2:
                            midpoints.add(new_word)
                            pre1[new_word].append(w)
                        elif new_word in words:
                            tmp.add(new_word)
                            pre1[new_word].append(w)
            for new_word in tmp:
                words.remove(new_word)
            if len(tmp) <= len(set2):
                    set1 = tmp
            else:
                set1, set2 = set2, tmp
                pre1, pre2 = pre2, pre1

            if midpoints:
                break

        if beginWord+'#' not in pre1:
            pre1, pre2 = pre2, pre1

        res = []
        for midpoint in midpoints:
            for path1 in self.get_paths(midpoint, beginWord, pre1):
                for path2 in self.get_paths(midpoint, endWord, pre2):
                    print(path1, path2)
                    res.append(path1[::-1] + path2[1:])
        return res

    def get_paths(self, start, end, pre):
        res = []
        def dfs(path):
            if path[-1] == end:
                res.append(path)
                return
            for word in pre[path[-1]]:
                dfs(path + [word])
        dfs([start])
        return res