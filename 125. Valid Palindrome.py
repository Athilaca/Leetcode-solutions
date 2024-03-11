class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=""
        s=s.lower()
        for i in s:
            if  i.isalnum():
                a+=i
        return a==a[::-1]
               
