class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        number=1
        while n>0:
            n=n-number
            number+=1
            if n>=0:
                count+=1
        return count 