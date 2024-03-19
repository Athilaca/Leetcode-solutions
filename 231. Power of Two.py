class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        while (2**x != n and x >= 0):
            if 2**x > n:
                return False
            x += 1 
        return True