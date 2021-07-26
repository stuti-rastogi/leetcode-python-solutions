import functools

class Solution:
    def comparator(self, log1, log2):
        words_log1 = log1.split(' ')
        words_log2 = log2.split(' ')
        if words_log1[1:] == words_log2[1:]:
            return -1 if (words_log1[0] < words_log2[0]) else 1
        return -1 if (words_log1[1:] < words_log2[1:]) else 1

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []

        for log in logs:
            words_in_log = log.split(' ')
            if words_in_log[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=functools.cmp_to_key(self.comparator))
        return (letter_logs + digit_logs)
