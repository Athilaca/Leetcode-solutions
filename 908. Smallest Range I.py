class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return 0 if max(nums) - min(nums) <= 2*k else max(nums) - min(nums) - 2*k