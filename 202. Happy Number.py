class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(len(str(n))>1):
            a=0
            for i in str(n):
                a+=int(i)**2
            n=a
        if n==1 or n==7:
            return True
        return False   