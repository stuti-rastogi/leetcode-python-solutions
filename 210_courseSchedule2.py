# DFS SOLUTION
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         graph = collections.defaultdict(list)
#         nextNodes = collections.defaultdict(list)

#         # traverse edge lists and populate
#         for pair in prerequisites:
#             graph[pair[0]].append(pair[1])
#             nextNodes[pair[1]].append(pair[0])

#         # print (graph)
#         # print (nextNodes)

#         stack = []
#         result = []

#         # starting nodes
#         for i in range(numCourses):
#             if i not in graph:
#                 stack.append(i)

#         while (stack):
#             curr = stack.pop()
#             print ("Curr: {}".format(curr))
#             result.append(curr)
#             for nextNode in nextNodes[curr]:
#                 # print ("nextNode: {}".format(nextNode))
#                 # print (graph[nextNode])
#                 graph[nextNode].remove(curr)
#                 # all possible paths to this next node are explored
#                 # add it to stack then
#                 if not graph[nextNode]:
#                     stack.append(nextNode)
#             # remove from further consideration
#             if curr in graph:
#                 graph.pop(curr)

#         if len(result) == numCourses:
#             return result
#         return []

# BFS SOLUTION
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == []:
            return [i for i in range(numCourses)]
        res = []

        indegree = [0] * numCourses

        result = dict()

        for i in range(len(prerequisites)):
            if prerequisites[i][1] in result:
                result[prerequisites[i][1]].append(prerequisites[i][0])
            else:
                result[prerequisites[i][1]] = [prerequisites[i][0]]
            indegree[prerequisites[i][0]] += 1

        queue = []
        for j in range(len(indegree)):
            if indegree[j] == 0:
                queue.append(j)

        while(len(queue) > 0):
            num = queue.pop(0)
            res.append(num)
            if num in result:
                neighbors = result[num]
            else:
                neighbors = []
            for i in range(len(neighbors)):
                indegree[neighbors[i]] -= 1
                if indegree[neighbors[i]] == 0:
                    queue.append(neighbors[i])

        if len(res) == numCourses:
            return res
        return []