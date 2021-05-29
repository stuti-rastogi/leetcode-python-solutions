class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        numsLen = len(nums)
        width = t + 1
        buckets = {}

        for i in range(numsLen):
            key = nums[i] // width
            if key in buckets:
                return True
            if key-1 in buckets and abs(nums[i] - buckets[key-1]) < width:
                return True
            if key+1 in buckets and abs(nums[i] - buckets[key+1]) < width:
                return True
            buckets[key] = nums[i]
            if i >= k:
                del buckets[nums[i-k]//width]

        return False
