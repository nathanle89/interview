"""

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

"""

import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        operation_counter = 0
        task_counter = {}
        max_queue = []

        for task in tasks:
            task_counter[task] = task_counter.get(task, 0) + 1

        for task in task_counter.keys():
            heapq.heappush(max_queue, (-task_counter[task], task))

        while len(max_queue) > 0:
            clock_counter = 0
            temp = []
            while clock_counter <= n:
                if len(max_queue) > 0:
                    priority, current_task = heapq.heappop(max_queue)

                    task_counter[current_task] -= 1
                    if task_counter[current_task] == 0:
                        del task_counter[current_task]
                    else:
                        temp.append((-task_counter[current_task], current_task))

                operation_counter += 1

                if len(max_queue) == 0 and len(temp) == 0:
                    break

                clock_counter += 1

            for task_tuple in temp:
                heapq.heappush(max_queue, task_tuple)

        return operation_counter


#IN PROGRESSSSSSSS


solution = Solution()

tasks = ["A","B","C","A","B"]
n = 2

tasks = ["A","A","A","B","B","B"]
n = 2
print solution.leastInterval(tasks, n)
