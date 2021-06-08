class Solution:
    def calculateId(self, num: int) -> int:
        """
            Id is position between 1 and 15
            node position is 2^(d-1) - 1 + p
            d = num // 100 - hundreds place
            p = (num // 10) % 10 - tens place
        """
        d = num // 100
        p = (num // 10) % 10
        return 2 ** (d-1) - 1 + p


    def pathSum(self, nums: List[int]) -> int:
        self.total = 0

        # v = num % 10 - units place
        nodes = {self.calculateId(num): num % 10 for num in nums}

        def dfs(position, curr_sum):
            curr_sum += nodes[position]
            # for a node at position p, children are at positions 2p & 2p+1
            left_child_pos = 2 * position
            right_child_pos = left_child_pos + 1
            if left_child_pos not in nodes and right_child_pos not in nodes:
                # found a leaf
                self.total += curr_sum
                return
            if left_child_pos in nodes:
                dfs(2*position, curr_sum)
            if right_child_pos in nodes:
                dfs(2*position+1, curr_sum)
            curr_sum -= nodes[position]

        dfs(1, 0)
        return self.total

