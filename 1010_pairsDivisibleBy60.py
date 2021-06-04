class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        count = 0
        for t in time:
            if t % 60 == 0:
                # check if a%60==0 && b%60==0
                count += remainders[0]
            else:
                # check if a%60+b%60==60
                count += remainders[60-t % 60]
            remainders[t % 60] += 1
        return count

        # O(n^2) - TLE
#         count = 0
#         time_len = len(time)

#         for i in range(time_len):
#             for j in range(i+1, time_len):
#                 if (time[i] + time[j]) % 60 == 0:
#                     count += 1
#         return count