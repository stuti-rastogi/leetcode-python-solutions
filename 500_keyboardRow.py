class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1='qwertyuiop'
        row2='asdfghjkl'
        row3='zxcvbnm'
        r=[]
        
        for i in words:
            if set(i.lower()).issubset(set(row1)):
                r.append(i)
            elif set(i.lower()).issubset(set(row2)):
                r.append(i)
            elif set(i.lower()).issubset(set(row3)):
                r.append(i)
        return r
    
#         if not words:
#             return []
#         alphabet = {1: ['q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p'],
#                     2: ['a', 's', 'd', 'f', 'g', 'h','j', 'k', 'l'],
#                     3: ['z', 'x', 'c', 'v', 'b', 'n','m']}
#         result = []
#         for word in words:
#             check = word.lower()
#             row = []
#             for i in alphabet.keys():
#                 if check[0] in alphabet[i]:
#                     row = alphabet[i]
#                     break
            
#             answer = True
#             for x in check:
#                 if x not in row:
#                     answer = False
#                     break
#             if answer:
#                 result.append(word)
        
#         return result
            