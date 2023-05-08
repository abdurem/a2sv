class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        
        queue = deque([("0000", 0)])
        visited = set("0000")
        
        while queue:
            (current, steps) = queue.popleft()
            if current == target:
                return steps
            for i in range(4):
                for move in (-1, 1):
                    new_digit = (int(current[i]) + move) % 10
                    new_combination = current[:i] + str(new_digit) + current[i+1:]
                    if new_combination not in dead_set and new_combination not in visited:
                        visited.add(new_combination)
                        queue.append((new_combination, steps + 1))
        
        return -1