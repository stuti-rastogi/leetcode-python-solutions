# from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # BRUTE FORCE - Time limit exceeded (32/34)
        ###########################################
        # s_length = len(s)
        # t_length = len(t)
        # if (s_length != t_length):
        #     return False
        # count = 0
        # done = []
        # for char in s:
        #     for i in range(t_length):
        #         if (char == t[i] and i not in done):
        #             count = count + 1
        #             done.append(i)
        #             break
        # if (count == t_length):
        #     return True
        # return False
        
        # SORTING
        ###########################################
        # s_sorted = "".join(sorted(s))
        # t_sorted = "".join(sorted(t))
        
        # s_len = len(s_sorted)
        # t_len = len(t_sorted)
        
        # if (s_len != t_len):
        #     return False
        
        # for i in range(s_len):
        #     if (s_sorted[i] != t_sorted[i]):
        #         return False
        # return True
    
        # ONE LINE SORTING
        ###########################################
        # return "".join(sorted(s))=="".join(sorted(t))
        
        # ONE LINE COUNTER
        ###########################################
        # return Counter(s) == Counter(t)
        
        # COUNTING CHAR COUNT
        ###########################################
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for char in alphabet:
            if(s.count(char) != t.count(char)):
                return False
        return True