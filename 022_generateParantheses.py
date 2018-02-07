class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        solution = []
        self.generateParenthesisRec(n,0,0,[],solution)
        return solution
    
    # backtracking method
    def generateParenthesisRec(self, n, openParentheses, closeParentheses, tempSolution, solution):
        if closeParentheses == n:
            solution.append(''.join(tempSolution))
            return
        if openParentheses <  n:
            tempSolution.append('(')
            self.generateParenthesisRec(n, openParentheses+1, closeParentheses, tempSolution, solution)
            tempSolution.pop()
        if closeParentheses < openParentheses:
            tempSolution.append(')')
            self.generateParenthesisRec(n, openParentheses, closeParentheses+1, tempSolution, solution)
            tempSolution.pop()