class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        s_itr = 0
        s_len = len(s)
        
        while (s_itr < s_len):
            s_char = s[s_itr]
            if not stack:
                stack.append([s_char, 1])
            else:
                # same character, increment count
                if s_char == stack[-1][0]:
                    new_count = stack[-1][1] + 1
                    if new_count == k:
                        stack.pop()
                    else:
                        stack[-1][1] = new_count
                else:
                    stack.append([s_char, 1])
            s_itr += 1
            
        # reconstruct string from stack
        str_list = []
        for el in stack:
            str_list += [el[0] for _ in range(el[1])]
            
        return "".join(str_list)