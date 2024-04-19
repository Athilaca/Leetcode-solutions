class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # a=int(num1)+int(num2)
        # return str(a)
        n1,n2=len(num1),len(num2)
        s=t=0
        for i in range(n1):
            o=ord(num1[i])-48
            a=s*10
            s=a+o
        for i in range(n2):
            o=ord(num2[i])-48
            a=t*10
            t=a+o
        return str(s+t)