class Solution(object):
    # do BFS till reach target
    # store length to each path
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        l = len(beginWord)
        
        # pre-processing
        generic_strs = collections.defaultdict(list)
        for word in wordList:
            for i in range(l):
                generic_strs[word[:i] + '*' + word[i+1:]].append(word)
                
        # bfs
        queue = collections.deque([(beginWord, 1)])
        visited = set()
        while queue:
            currentWord, level = queue.popleft()
            visited.add(currentWord)
            for i in range(l):
                next_word = currentWord[:i] + '*' + currentWord[i+1:]
                for neighbor in generic_strs[next_word]:
                    if neighbor == endWord:
                        return level+1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level+1))
        return 0
