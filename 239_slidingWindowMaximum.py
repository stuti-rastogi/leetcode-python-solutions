from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if k == 1:
            return nums

        output = []
        # deque - in decreasing order from front to back
        # store all useful elements of current window of size k
        # useful elements are elements smaller to the max element but only to the right
        # so these could become potential max values in the next window
        queue = collections.deque()

        # first window
        for i in range(k):
            # remove all the elements from the back
            # that are smaller than this element
            # previous smaller elements are useless now
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            # append index of curr element at the back
            queue.append(i)

        # process from index k to n-1
        for i in range(k, n):
            # the element at the front of the list is the
            # max of the previous window
            # so append to output
            # DON'T POP YET!
            output.append(nums[queue[0]])

            # remove elements out of this window
            # since they are ordered we need to check each
            # this is why we store indices
            while queue and queue[0] <= i-k:
                queue.popleft()

            # remove elements smaller than this element
            # elements to the left that are smaller are useless now
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()

            # add index of curr element at the back
            queue.append(i)

        # append the max of the last window
        output.append(nums[queue[0]])
        return output


        # max_sliding_window = []
        # end_idx = len(nums) - k
        # for idx in range(end_idx + 1):
        #     max_sliding_window.append(max(nums[idx:idx+k]))
        # return max_sliding_window