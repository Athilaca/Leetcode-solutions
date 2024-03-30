class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while n:
            if 3**i==n:
                return True
            elif 3**i>n:
                return False
            i+=1 