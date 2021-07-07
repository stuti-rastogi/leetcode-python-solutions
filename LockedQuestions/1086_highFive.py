class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        studentScores = collections.defaultdict(list)
        for studentId, studentScore in items:
            studentScores[studentId].append(studentScore)
            
        highFiveOutput = []
        for student in studentScores:
            highFiveAvg = sum(sorted(studentScores[student], reverse=True)[:5]) // 5
            highFiveOutput.append([student, highFiveAvg])
            
        return sorted(highFiveOutput)

    # studentScores = collections.defaultdict(list)
    # for idx, val in items:
    #     heapq.heappush(studentScores[idx], val)
        
    #     if len(studentScores[idx]) > 5:
    #         heapq.heappop(studentScores[idx])
    
    # return [[i, sum(studentScores[i]) // len(studentScores[i])] for i in sorted(studentScores)]
