class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = {"a","e","i","o","u","A","E","I","O","U"}
        s_vowel = [v for v in s if v in vowel] 
        j=len(s_vowel)-1
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in vowel:
                s_list[i] = s_vowel[j]
                j -=1
        return "".join(s_list)