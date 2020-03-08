from collections import Counter
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-(c+d)] for c in C for d in D)

        # without collections
        # abSum = {}
        # for a in A:
        #     for b in B:
        #         check = a+b
        #         if check in abSum:
        #             abSum[check] += 1
        #         else:
        #             abSum[check] = 1

        # count = 0
        # for c in C:
        #     for d in D:
        #         check = -(c+d)
        #         if (check in abSum):
        #             count += abSum[check]