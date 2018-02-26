class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # O(nklgk) - where k is max length of string in strs
        dict = {}
        # O(n) - for loop
        for string in strs:
            check = ''.join(sorted(string))         # sorting takes O(klgk)
            if check in dict:
                dict[check].append(string)
            else:
                dict[check] = [string]
        return list(dict.values())

# tuple of 26 entries - count of each letter
# O(nk)
# class Solution:
#     def groupAnagrams(strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             ans[tuple(count)].append(s)
#         return ans.values()