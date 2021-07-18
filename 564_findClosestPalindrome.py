class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def buildPalindrome(baseStr, isEvenLen):
            if isEvenLen:
                return baseStr + ''.join(reversed(baseStr))
            else:
                return baseStr[:-1] + baseStr[-1] + ''.join(reversed(baseStr[:-1]))


        num = int(n)
        # for cases 1,2,3,...,10 and 100, 1000, 10000, etc.
        if num <= 10 or (num % 10 == 0 and n[0] == '1' and int(n[1:]) == 0):
            return str(num-1)
        # for cases 11, 101, 1001, etc.
        elif num == 11 or (num % 10 == 1 and n[0] == '1' and int(n[1:-1]) == 0):
            return str(num-2)
        # for cases 9, 99, 999, etc.
        elif n[0] == '9' and n[0] * len(n) == n:
            return str(num+2)

        midLen = len(n) // 2
        isEvenLen = (len(n) % 2 == 0)
        if isEvenLen:
            baseStr = n[0:midLen]
        else:
            baseStr = n[0:midLen+1]

        if buildPalindrome(baseStr, isEvenLen) == n:
            isNPalindrome = True
        else:
            isNPalindrome = False

        if isNPalindrome:
            baseCandidates = [int(baseStr)-1, int(baseStr)+1]
        else:
            baseCandidates = [int(baseStr)-1, int(baseStr), int(baseStr)+1]

        minDiff = float('inf')
        for base in baseCandidates:
            possiblePalindrome = int(buildPalindrome(str(base), isEvenLen))
            if abs(possiblePalindrome - num) < minDiff:
                minDiff = abs(possiblePalindrome - num)
                minBase = str(base)

        return buildPalindrome(minBase, isEvenLen)
