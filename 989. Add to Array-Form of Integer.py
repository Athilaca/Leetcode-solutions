class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        c=[]
        a=''.join(map(str,num)) 
        b=int(a)+k
        c= [int(digit) for digit in str(b)]
        return(c)  