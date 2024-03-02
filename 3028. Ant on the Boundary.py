class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        step=0
        for i in nums:
            step+=i
            if step==0:
                count+=1
        return count 