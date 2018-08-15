class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic={}
        for i,wd in enumerate(words):
            if len(wd) in dic:
                dic[len(wd)][wd]=i
            else:
                dic[len(wd)]={wd:i}
        ans=[]
        # same length
        for k in dic:
            for wd in dic[k]:
                if wd[::-1] in dic[k]:
                    i=dic[k][wd]
                    j=dic[k][wd[::-1]]
                    if i!=j:
                        ans.append([i,j])
        # diff length
        for k in dic:
            for l in range(k):
                if l in dic:
                    for wd in dic[k]:
                        left=wd[:-(l+1):-1]
                        right=wd[:l][::-1]
                        if left in dic[l]:
                            leftwd=left+wd
                            if leftwd==leftwd[::-1]:
                                ans.append([dic[l][left],dic[k][wd]])
                        if right in dic[l]:
                            rightwd=wd+right
                            if rightwd==rightwd[::-1]:
                                ans.append([dic[k][wd],dic[l][right]])
        return ans