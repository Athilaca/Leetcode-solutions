class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=set(nums)
        b=list(a)
        b.sort(reverse=True)

        if len(b)>=3:
          return b[2] 
        else:
            return max(b)  