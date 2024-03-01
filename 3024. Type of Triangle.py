class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if nums[0]==nums[1]==nums[2]:
            return "equilateral"
        elif nums[0]==nums[1] or nums[1]==nums[2]:
            return "isosceles"
        else:
            return "scalene"            
        