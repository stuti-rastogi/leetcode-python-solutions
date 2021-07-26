import itertools

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visited_websites = collections.defaultdict(list)
        for idx, user in enumerate(username):
            user_visited_websites[user].append((website[idx], timestamp[idx]))

        # sort by time stamp for each user to get 3-seq
        for user in user_visited_websites:
            user_visited_websites[user].sort(key=lambda x: x[1])

        print (user_visited_websites)

        # create 3-sequences for each user

        three_sequence_to_count = collections.defaultdict(int)
        for user in user_visited_websites:
            websites = [item[0] for item in user_visited_websites[user]]
            for seq in set(itertools.combinations(websites, 3)):
                three_sequence_to_count[seq] += 1

        max_count, max_sequence = -1, None
        for seq in three_sequence_to_count:
            if three_sequence_to_count[seq] > max_count:
                max_count = three_sequence_to_count[seq]
                max_sequence = seq
            elif three_sequence_to_count[seq] == max_count:
                max_sequence = min(max_sequence, seq)
        return max_sequence
