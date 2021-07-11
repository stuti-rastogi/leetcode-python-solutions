"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], employee_id: int) -> int:
        id_employee_map = {}
        for employee in employees:
            id_employee_map[employee.id] = employee

        stack = []
        stack.append(employee_id)
        importance = 0
        while stack:
            curr_employee = id_employee_map[stack.pop()]
            importance += curr_employee.importance
            for subordinate_id in curr_employee.subordinates:
                stack.append(subordinate_id)

        return importance
