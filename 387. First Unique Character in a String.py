class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={}
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]]+=1
            else:
                a[s[i]]=1
        for i in range(len(s)):
            if a[s[i]]==1:
                return i
        return -1 