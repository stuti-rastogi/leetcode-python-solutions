class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # validDecoding[i] is the count of decodings of substring s[i:]
        countDecoding = [-1] * (n+1)
        countDecoding[-1] = 1

        for i in range(n-1, -1, -1):
            count1 = countDecoding[i+1] if 1 <= int(s[i:i+1]) <= 9 else 0
            count2 = countDecoding[i+2] if 10 <= int(s[i:i+2]) <= 26 else 0
            countDecoding[i] = count1 + count2
        return countDecoding[0]