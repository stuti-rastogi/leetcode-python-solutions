class Solution:
    # Function to find precedence
    # of operators.
    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        # brackets
        return 0


    # Function to perform arithmetic
    # operations.
    def applyOp(self, a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return int(a / b)


    # Function that returns value of
    # expression after evaluation.
    def calculate(self, tokens: str) -> int:
        # stack to store integer values.
        values = []
        # stack to store operators.
        ops = []
        i = 0

        while i < len(tokens):
            # Current token is a whitespace,
            # skip it.
            if tokens[i] == ' ':
                i += 1
                continue
            # Current token is an opening
            # brace, push it to 'ops'
            elif tokens[i] == '(':
                ops.append(tokens[i])

            # Current token is a number, push
            # it to stack for numbers.
            elif tokens[i].isdigit():
                val = 0
                # There may be more than one
                # digits in the number.
                while (i < len(tokens) and tokens[i].isdigit()):
                    val = (val * 10) + int(tokens[i])
                    i += 1
                values.append(val)

                # right now the i points to the character next to the digit,
                # since the outer loop also increases the i, we would skip one token position;
                # we need to decrease the value of i by 1 to correct the offset.
                i-=1

            # Closing brace encountered,
            # solve entire brace.
            elif tokens[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.applyOp(val1, val2, op))
                # pop opening brace.
                ops.pop()
            # Current token is an operator.
            else:
                # While top of 'ops' has same or greater precedence to current
                # token, which is an operator.
                # Apply operator on top of 'ops' to top two elements in values stack.
                while (len(ops) != 0 and self.precedence(ops[-1]) >= self.precedence(tokens[i])):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.applyOp(val1, val2, op))
                # Push current token to 'ops'.
                ops.append(tokens[i])
            i += 1

        # Entire expression has been parsed
        # at this point, apply remaining ops
        # to remaining values.
        while len(ops) != 0:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
            values.append(self.applyOp(val1, val2, op))

        # Top of 'values' contains result,
        # return it.
        return values[-1]



# class Solution:
#     def calculate(self, s: str) -> int:
#         s_len = len(s)
#         # level 1 is + and -
#         # level 2 is * and /
#         level_1_result = 0
#         level_2_result = 1

#         level_1_op = '+'
#         level_2_op = '*'

#         s_index = 0
#         while (s_index < s_len):
#             char = s[s_index]
#             if char.isdigit():
#                 curr_value = int(char)
#                 while s_index+1 < s_len and s[s_index+1].isdigit():
#                     curr_value = (curr_value * 10) + int(s[s_index+1])
#                     s_index += 1
#                 # any operand is made part of level 2 by default
#                 # curr_value == 0 -> True, 1 picked from (curr_value, 1)
#                 if level_2_op == '/':
#                     level_2_result = (level_2_result / (curr_value, 1)[curr_value == 0])
#                 else:
#                     level_2_result = level_2_result * curr_value

#             elif char == '(':
#                 # a new sub-expression starts here
#                 start = s_index + 1
#                 count_brackets = 0
#                 while s_index < s_len:
#                     if s[s_index] == '(':
#                         count_brackets += 1
#                     elif s[s_index] == ')':
#                         count_brackets -= 1
#                     if count_brackets == 0:
#                         # parenthesis matched up, get the expression
#                         break
#                     s_index += 1
#                 curr_value = self.calculate(s[start:s_index])
#                 if level_2_op == '/':
#                     level_2_result = (level_2_result / (curr_value, 1)[curr_value == 0])
#                 else:
#                     level_2_result = level_2_result * curr_value

#             elif char in ['*', '/']:
#                 # need to update level 2 operator
#                 level_2_op = char

#             elif char in ['+', '-']:
#                 # evaluate level 2 partial result with level 1 op
#                 level_1_result = level_1_result + level_2_result if level_1_op == '+' else level_1_result - level_2_result
#                 # update level 1 op
#                 level_1_op = char
#                 # reset level 2
#                 level_2_result = 1
#                 level_2_op = '*'

#             s_index += 1

#         # finally combine level 1 and 2 and return
#         return level_1_result + level_2_result if level_1_op == '+' else level_1_result - level_2_result
