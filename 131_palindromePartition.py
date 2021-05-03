class Solution:
    # Backtracking with DP
    # Time complexity: O(n * 2^n) - https://stackoverflow.com/questions/24591616/whats-the-time-complexity-of-this-algorithm-for-palindrome-partitioning
    # See: https://leetcode.com/problems/palindrome-partitioning/solution/
    # For variation with only number of cuts: https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # dp 2D array to avoid checking for palindrome condition on same substring
        isPalindrome = [[False for i in range(n)] for i in range(n)]
        result = []
        self.dfs(s, 0, isPalindrome, [], result)
        return result


    def dfs (self, s, start, isPalindrome, currList, result):
        if start >= len(s):
            result.append(currList.copy())
        for end in range(start, len(s)):
            # For substring s[start:end+1], it is a palindrome:
            # a) if first and last characters match and s[start+1:end] is a palindrome OR
            # b) if first and last characters match but substring is of length 1, 2 or 3
            if (s[start] == s[end]) and ((end <= start+2) or (isPalindrome[start+1][end-1])):
                isPalindrome[start][end] = True
                # This substring is part of a possible partition, so append to current list
                currList.append(s[start:end+1])
                # Partition at end, so new start becomes end+1
                self.dfs(s, end+1, isPalindrome, currList, result)
                currList.pop()
