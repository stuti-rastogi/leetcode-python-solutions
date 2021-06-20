class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        str_len = len(s)
        result = []
        curr_result = []

        def backtrack(index, curr_result):
            if index == str_len:
                result.append("".join(curr_result))
                return
            if s[index].isdigit():
                curr_result.append(s[index])
                backtrack(index+1, curr_result)
                curr_result.pop()
            else:
                # lower case path
                curr_result.append(s[index].lower())
                backtrack(index+1, curr_result)
                curr_result.pop()

                # upper case path
                curr_result.append(s[index].upper())
                backtrack(index+1, curr_result)
                curr_result.pop()

        backtrack(0, curr_result)
        return result


        # permutations = [[]]
        # for c in s:
        #     curr_len = len(permutations)
        #     if c.isalpha():
        #         for i in range(curr_len):
        #             permutations.append(permutations[i].copy())
        #             permutations[i].append(c.lower())
        #             permutations[curr_len+i].append(c.upper())
        #     else:
        #         for i in range(curr_len):
        #             permutations[i].append(c)
        # return list(map("".join, permutations))
