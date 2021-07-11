class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        num_cards = len(cardPoints)
        start_rear_set = num_cards-k
        front_score = 0
        rear_score = sum(cardPoints[start_rear_set:])

        curr_score = front_score + rear_score
        max_score = curr_score

        for i in range(k):
            curr_score = curr_score + cardPoints[i] - cardPoints[start_rear_set]
            max_score = max(max_score, curr_score)
            start_rear_set += 1

        return max_score


#         num_cards = len(cardPoints)
#         front_set = [0 for _ in range(k+1)]
#         rear_set = [0 for _ in range(k+1)]

#         for i in range(1, k+1):
#             front_set[i] = front_set[i-1] + cardPoints[i-1]
#             rear_set[i] = rear_set[i-1] + cardPoints[num_cards-i]

#         max_score = 0
#         for i in range(k+1):
#             curr_score = front_set[i] + rear_set[k-i]
#             max_score = max(max_score, curr_score)

#         return max_score