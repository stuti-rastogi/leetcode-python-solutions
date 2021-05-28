class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # binary_strings = []
        # for num in data:
        #     binary_strings.append(format(num, "08b"))
        # print (binary_strings)

        num_bytes = 0

        mask1 = 1 << 7
        mask2 = 1 << 6

        for num in data:
            # num_bytes is 0 at the start of a new character, count # 1s
            if num_bytes == 0:
                mask = 1 << 7
                while mask & num:
                    num_bytes += 1
                    mask = mask >> 1
                # 1 byte character
                if num_bytes == 0:
                    continue
                if num_bytes == 1 or num_bytes > 4:
                    return False
            # we are in the middle of an ongoing character
            else:
                # first two MSBs are not "10"
                if not ((num & mask1) and not (num & mask2)):
                    return False
            num_bytes -= 1

        return num_bytes == 0
