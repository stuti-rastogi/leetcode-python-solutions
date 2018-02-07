class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # no extra space:

        # ans = self.nums[:]
        # n = len(ans)
        # for i in range(n-1, -1, -1):
        #     j = random.randint(0,i)
        #     ans[i], ans[j] = ans[j], ans[i]
        # return ans
        
        # auxiliary array
        answer, temp = [], [] + self.nums
        size = len(temp)
        for _ in range(size):
            index = random.randint(0, len(temp) - 1)
            answer.append(temp.pop(index))
        return answer


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()