class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if not endWord or not beginWord or not wordList or endWord not in wordList \
            or beginWord == endWord:
            return []

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Shortest path, BFS
        ans = []
        queue = collections.deque()
        queue.append((beginWord, [beginWord]))
        visited = set([beginWord])

        while queue and not ans:
            length = len(queue)
            localVisited = set()
            for _ in range(length):
                word, path = queue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord == endWord:
                            ans.append(path+[endWord])
                        if nextWord not in visited:
                            localVisited.add(nextWord)
                            queue.append((nextWord, path+[nextWord]))
            visited = visited.union(localVisited)

        return ans
