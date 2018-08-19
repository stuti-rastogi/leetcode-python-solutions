class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dic = {}
        start = max_len = 0
        
        for i, c in enumerate(s):
            if c in dic and start <= dic[c]:
                start = dic[c]+1
            else:
                max_len = max(max_len, i-start+1)
            dic[c] = i
        
        return max_len