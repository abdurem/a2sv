class Solution:
    def dailyTemperatures(self, tmp: List[int]) -> List[int]:
        ans=[0]*len(tmp)
        day=[]
        
        for today,tmp_today in enumerate(tmp):
            
            while day and tmp[day[-1]] < tmp_today:
                past = day.pop()
                ans[past] = today-past
            
            day.append(today)
        
        return ans