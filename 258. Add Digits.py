class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num))==1:
            return num
        else:
            s=0
            for i in str(num):
                s+=int(i)
            return self.addDigits(s)