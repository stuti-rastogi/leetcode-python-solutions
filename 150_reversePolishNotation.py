class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for c in tokens:
            if c in ['+', '-', '*', '/']:
                op2 = stack.pop()
                op1 = stack.pop()
                if c == '+':
                    stack.append(op1+op2)
                elif c == '-':
                    stack.append(op1-op2)
                elif c == '*':
                    stack.append(op1*op2)
                else:
                    stack.append(int(op1/op2))
            else:
                stack.append(int(c))
        return stack[0]