class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        preferredFriends = {}
        
        for x, y in pairs:
            preferredFriends[x] = set(preferences[x][:preferences[x].index(y)])
            preferredFriends[y] = set(preferences[y][:preferences[y].index(x)])
            
        unhappyCount = 0
        for person in preferredFriends:
            for preferredPerson in preferredFriends[person]:
                if person in preferredFriends[preferredPerson]:
                    unhappyCount += 1
                    break
        return unhappyCount
