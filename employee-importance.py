"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {employee.id: employee for employee in employees}
        def dfs(id):
            employee = emp_map[id]
            return employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)
        return dfs(id)