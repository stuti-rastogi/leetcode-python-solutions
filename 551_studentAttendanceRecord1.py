class Solution:
    def checkRecord(self, s: str) -> bool:
        s_len = len(s)
        count_absences = 0
        count_late_days = 0

        for idx in range(s_len):
            if s[idx] == 'L':
                count_late_days += 1
                if count_late_days == 3:
                    return False
            else:
                count_late_days = 0
                if s[idx] == 'A':
                    count_absences += 1
                    if count_absences >= 2:
                        return False

        return True
