class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
#         mapping = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
#         result = []
#         for x in digits:
#             if not result:
#                 result = result + list(mapping[x])
#             else:
#                 perm = []
#                 for word in result:
#                     for c in list(mapping[x]):
#                         newWord = word + c
#                         perm.append(newWord)
#                 result = perm
#         return result

        numletter = {
                    '2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'
                   }
        
        letters = [numletter[i] for i in digits]
        from functools import reduce
        if digits:
            if len(digits) == 1:
                return list(numletter[digits])
            else:
                return reduce((lambda x, y: [i + j for i in x for j in y]), letters) 
        else:
            return []