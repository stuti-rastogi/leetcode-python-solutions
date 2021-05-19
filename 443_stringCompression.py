class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return n

        # index where we write the char and count
        toWrite = 0
        # traversing
        i = 0
        while i < n:
            chars[toWrite] = chars[i]
            count = 1

            toWrite += 1
            i += 1

            while (i < n and chars[i] == chars[toWrite-1]):
                i += 1
                count += 1

            if count > 1:
                charCount = str(count)
                for c in charCount:
                    chars[toWrite] = c
                    toWrite += 1

        return toWrite
