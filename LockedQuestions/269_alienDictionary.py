class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # lexicographic order is finding topological sort in a DAG
        indegree = {}
        adjacency = {}

        # initialization
        for word in words:
            for c in word:
                indegree[c] = 0
                adjacency[c] = []

        num_words = len(words)
        for index in range(num_words-1):
            word1 = words[index]
            word2 = words[index+1]
            found = False
            min_len = min(len(word1), len(word2))
            for it in range(min_len):
                char1 = word1[it]
                char2 = word2[it]
                if char1 != char2:
                    # word1 is before word2 and they differ for the first time at char1/2
                    # so in graph of lexicographical ordering, char1 -> char2 is an edge
                    # update indegree and adjacency to indicate this
                    found = True
                    indegree[char2] += 1
                    adjacency[char1].append(char2)
                    break
            # handle case like ["abc", "ab"]
            if not found and len(word2) < len(word1):
                return ""

        # find nodes with 0 indegree
        queue = collections.deque()
        for c in adjacency:
            if indegree[c] == 0:
                queue.append(c)

        output = []
        while queue:
            curr_letter = queue.popleft()
            output.append(curr_letter)

            for neighbor in adjacency[curr_letter]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # check if all characters were part of output
        if len(indegree) != len(output):
            return ""
        else:
            return "".join(output)
