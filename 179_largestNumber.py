class ConcatenationComparator(str):
    def __lt__(a, b):
        return a+b > b+a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strings = map(str, nums)
        largestNum = "".join(sorted(strings, key=ConcatenationComparator))
        return "0" if largestNum[0] == "0" else largestNum
