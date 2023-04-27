class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        que = deque(rooms[0])
        keys = set([0])

        while que:
            door = que.popleft()
            keys.add(door)
            for d in rooms[door]:
                if d not in keys:
                    que.append(d)
        
        return len(keys) == len(rooms)