class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        processed_tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])
        # priority is the processing time, and then index
        # min heap of (duration, index)
        available_tasks = []
        curr_task = 0
        order = []
        cpu_time = processed_tasks[0][0]

        while len(order) < len(processed_tasks):
            while (curr_task < len(processed_tasks) and (processed_tasks[curr_task][0] <= cpu_time)):
                heapq.heappush(available_tasks, (processed_tasks[curr_task][1], processed_tasks[curr_task][2]))
                curr_task += 1

            if available_tasks:
                duration, index = heapq.heappop(available_tasks)
                order.append(index)
                cpu_time += duration
            elif curr_task < len(processed_tasks):
                cpu_time = processed_tasks[curr_task][0]

        return order
