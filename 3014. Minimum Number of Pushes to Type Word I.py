class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        if len(word) <= 8:
            return len(word)
        
        if 8 < len(word) <= 16:
            return 8 + ((len(word) - 8) * 2)
        
        if 16 < len(word) <= 24:
            return 24 + ((len(word) - 16) * 3)
        
        else:
            return 48 + ((len(word) - 24) * 4)
        