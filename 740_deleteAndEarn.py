class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # NUMRANGE = 10000
        # counts = collections.Counter(nums)
        # prev = 0
        # curr = 0
        # for value in range(NUMRANGE+1):
        #     prev, curr = curr, max(prev + (value * counts[value]), curr)
        # return curr
        
        counts = collections.Counter(nums)
        # we need to keep track of the last number in sorted order we saw
        prev = None
        taking_num = 0
        not_taking_num = 0

        for num in sorted(counts):
            if num-1 != prev:
                taking_num, not_taking_num = max(taking_num, not_taking_num) + (num * counts[num]), max(taking_num, not_taking_num)
            else:
                # if last number we saw was num-1, we can't get points for both
                # so taking num means not taking num and curr value
                # not taking num could mean max of either of the cases before because it won't matter
                taking_num, not_taking_num = not_taking_num + (num * counts[num]), max(taking_num, not_taking_num)
            prev = num
        return max(taking_num, not_taking_num)
