import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # freq = collections.Counter(words)
        # return [item[0] for item in heapq.nsmallest(k, (freq.items()), key=lambda x: (x[1] * -1, x[0]))]

        # sorted_freq = [item[0] for item in sorted(freq.items(), key=lambda x: (x[1] * -1, x[0]))][:k]
        # return sorted_freq

        buckets = [[] for i in range(len(words)+1)]
        freq = collections.Counter(words)
        for item, f in freq.items():
            buckets[f].append(item)
        for bucket in buckets:
            bucket.sort()
        flattened_list = [x for bucket in buckets[::-1] for x in bucket]
        return flattened_list[:k]

