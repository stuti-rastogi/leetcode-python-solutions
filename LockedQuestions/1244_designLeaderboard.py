class Leaderboard:
    def __init__(self):
        self.player_scores = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.player_scores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for score in self.player_scores.values():
            if len(heap) < K:
                heapq.heappush(heap, score)
            else:
                heapq.heappushpop(heap, score)
        return sum(heap)


    def reset(self, playerId: int) -> None:
        self.player_scores.pop(playerId)


# class Leaderboard:
#     def __init__(self):
#         self.player_scores = collections.defaultdict(int)

#     def addScore(self, playerId: int, score: int) -> None:
#         self.player_scores[playerId] += score

#     def top(self, K: int) -> int:
#         return sum([x[1] for x in sorted(self.player_scores.items(), key=lambda x: -x[1])[:K]])

#     def reset(self, playerId: int) -> None:
#         self.player_scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
