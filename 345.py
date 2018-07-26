class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = set('aeiouAEIOU')
        j = len(s) - 1
        ret = [0 for x in range(len(s))] 
        for i in range(len(s)):
            ret[i] = s[i]
            if s[i] in vowel:
                while(s[j] not in vowel):
                    j -= 1
                ret[i] = s[j]
                j -= 1 
        return ''.join(ret)