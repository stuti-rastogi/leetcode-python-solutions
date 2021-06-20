class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = [w[0]]
        for weight in w[1:]:
            self.prefix_sums.append(weight+self.prefix_sums[-1])
        self.total_sum = self.prefix_sums[-1]


    def pickIndex(self) -> int:
        target_value = random.random() * self.total_sum
        return bisect.bisect(self.prefix_sums, target_value)

    # # TLE
    # def __init__(self, w: List[int]):
    #     self.uniform_pick = []
    #     for i in range(len(w)):
    #         for _ in range(w[i]):
    #             self.uniform_pick.append(i)
    #     self.bound = len(self.uniform_pick) - 1

    # def pickIndex(self) -> int:
    #     rand_index = random.randint(0, self.bound)
    #     return self.uniform_pick[rand_index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()