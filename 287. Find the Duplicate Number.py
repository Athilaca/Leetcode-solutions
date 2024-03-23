class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=set()
        for i in nums:
            if i in a :
                return i
            else:
                a.add(i)  