from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # if not nums or not k:
        #     return None
        # # return [i[0] for i in Counter(nums).most_common(k)]
        # return [x for x, count in sorted(Counter(nums).items(), key = lambda y: y[1], reverse = True)[ : k]]

        heap = []
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1

        for key in dic:
            heapq.heappush(heap,(-dic[key],key))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        # Heapq implementation already does the above
        # return heapq.nlargest(k, freq.keys(), key=freq.get)

        # Alternate method, like bucket sort
        # O(n) storage since we know frequencies can be 0 to n
        # buckets = [[] for i in range(len(nums) + 1)]
        # for n, f in freq.items():
        #     buckets[f].append(n)
        # flatten = [item for bucket in buckets[::-1] for item in bucket]
        # return flatten[:k]
