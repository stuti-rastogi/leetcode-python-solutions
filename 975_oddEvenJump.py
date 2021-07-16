class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        arr_len = len(arr)
        next_higher = [0 for _ in range(arr_len)]
        next_lower = [0 for _ in range(arr_len)]

        stack = []
        for _, idx in sorted((val, i) for i, val in enumerate(arr)):
            while stack and stack[-1] < idx:
                next_higher[stack.pop()] = idx
            stack.append(idx)

        stack = []
        for _, idx in sorted((-val, i) for i, val in enumerate(arr)):
            while stack and stack[-1] < idx:
                next_lower[stack.pop()] = idx
            stack.append(idx)

        odd_jumps = [False for _ in range(arr_len)]
        even_jumps = [False for _ in range(arr_len)]

        odd_jumps[-1] = True
        even_jumps[-1] = True

        for idx in range(arr_len-2, -1, -1):
            odd_jumps[idx] = even_jumps[next_higher[idx]]
            even_jumps[idx] = odd_jumps[next_lower[idx]]

        return sum(odd_jumps)
