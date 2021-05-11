class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # if not digits:
        #     return []

        # mapping = {
        #     '1': [],
        #     '2': ['a', 'b', 'c'],
        #     '3': ['d', 'e', 'f'],
        #     '4': ['g', 'h', 'i'],
        #     '5': ['j', 'k', 'l'],
        #     '6': ['m', 'n', 'o'],
        #     '7': ['p', 'q', 'r', 's'],
        #     '8': ['t', 'u', 'v'],
        #     '9': ['w', 'x', 'y', 'z']
        # }

        # result = ['']
        # for d in digits:
        #     letters = mapping[d]
        #     updatedResult = []
        #     for candidate in result:
        #         for letter in letters:
        #             updatedResult.append(candidate + letter)
        #     result = updatedResult

        # return result


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
