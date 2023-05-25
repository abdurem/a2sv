class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        ladder_used = []
        bricks_needed = 0

        for i in range(n - 1):
            height_diff = heights[i + 1] - heights[i]

            if height_diff > 0:
                heapq.heappush(ladder_used, height_diff)

                if len(ladder_used) > ladders:
                    bricks_needed += heapq.heappop(ladder_used)

                if bricks_needed > bricks:
                    return i

        return n - 1