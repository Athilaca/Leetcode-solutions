class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a="qwertyuiopQWERTYUIOP"
        b="asdfghjklASDFGHJKL"
        c="zxcvbnmZXCVBNM"
        f=''
        s=''
        t=''
        out=[]
        for i in words:
            for w in i:
                if w in a:
                    f+=w
                elif w in b:
                    s+=w
                elif w in c:
                    t+=w   
            if s==i or f==i or t==i:
                out.append(i)
            f,s,t="","",""
        return out 