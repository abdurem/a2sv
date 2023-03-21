class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted(list(range(len(intervals))), key = lambda x: intervals[x][0])
        ans = []
        for start, end in intervals:
            
            l, r = 0, len(starts) - 1
            
            while l <= r:
                
                mid = (l + r) //2
                idx = starts[mid]
                
                if intervals[idx][0] < end:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            ans.append(starts[l]) if l < len(intervals) else ans.append(-1)
        return ans