class Solution:
    def combinationSum(self, candidates, target):
#         candidates.sort()
#         dp = [[[]]] + [[] for i in range(target)]
        
#         for i in range(1, target + 1):
#             for number in candidates:
#                 if number > i: 
#                     break
#                 for L in dp[i - number]:
#                     if not L or number >= L[-1]: 
#                         dp[i] = dp[i] + [L + [number]]
#         return dp[target]
    
        res = []
        candidates.sort()
        def dfs(remain, stack):
            if not remain:
                res.append(stack)
                return 
            for item in candidates:
                if item > remain:
                    break
                elif not stack or item >= stack[-1]:
                    dfs(remain - item, stack + [item])
        dfs(target, [])
        return res