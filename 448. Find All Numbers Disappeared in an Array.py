class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=set(nums) 
        b=set(range(1,len(nums)+1)) 
        return list(b-a)    