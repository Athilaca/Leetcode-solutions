class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l=len(s)-1
        r=0
        while r<l:
            if not s[l].isalpha():
                l-=1
            elif not s[r].isalpha():
                r+=1
            else:
                s[l],s[r]=s[r],s[l] 
                l-=1
                r+=1
        return "".join(s)