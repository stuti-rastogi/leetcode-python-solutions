class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        currVal = 0
        stack = []
        operator = '+'
        for i in range(n):
            if s[i].isdigit():
                currVal = currVal * 10 + int(s[i])
            if s[i] in "+-*/" or i == n-1:
                if operator == "+":
                    stack.append(currVal)
                elif operator == "-":
                    stack.append(-currVal)
                elif operator == "*":
                    stack.append(stack.pop() * currVal)
                else:
                    stack.append(int(stack.pop() / currVal))
                currVal = 0
                operator = s[i]
        return sum(stack)
