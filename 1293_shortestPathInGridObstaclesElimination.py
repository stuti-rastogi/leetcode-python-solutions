class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if rows == 1 and cols == 1:
            return 0

        if k > rows+cols-2:
            return rows+cols-2

        visited = set()
        queue = collections.deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        step_count = 0

        queue.append((0, 0, k))
        visited.add((0, 0, k))

        while queue:
            curr_queue_len = len(queue)
            for _ in range(curr_queue_len):
                curr_x, curr_y, k_rem= queue.popleft()

                if curr_x == rows-1 and curr_y == cols-1:
                    return step_count

                for direction in directions:
                    new_x = curr_x + direction[0]
                    new_y = curr_y + direction[1]

                    if (0 <= new_x < rows and 0 <= new_y < cols):
                        if grid[new_x][new_y] == 1 and k_rem > 0 and (new_x, new_y, k_rem-1) not in visited:
                            queue.append((new_x, new_y, k_rem-1))
                            visited.add((new_x, new_y, k_rem-1))
                        elif grid[new_x][new_y] == 0 and (new_x, new_y, k_rem) not in visited:
                            queue.append((new_x, new_y, k_rem))
                            visited.add((new_x, new_y, k_rem))
            step_count += 1
        return -1
