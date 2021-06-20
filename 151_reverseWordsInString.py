class Solution:
    def reverse_str(self, s: str) -> str:
        if not s:
            return ""
        s_list = list(s.strip())
        s_len = len(s)
        mid = s_len // 2
        for i in range(mid):
            s_list[i], s_list[s_len-1-i] = s_list[s_len-1-i], s_list[i]
        return "".join(s_list)

    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_reverse = self.reverse_str(s)
        output = []
        start = 0
        for index, c in enumerate(s_reverse):
            if c == ' ':
                reversed_word = self.reverse_str(s_reverse[start:index])
                if reversed_word:
                    output.append(reversed_word)
                start = index+1
        output.append(self.reverse_str(s_reverse[start:]))
        return " ".join(output)


    # PYTHON 1 LINER
    # def reverseWords(self, s: str) -> str:
    #     return " ".join(s.split()[::-1])