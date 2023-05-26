class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        task_order = []
        heap = []
        start = 0
        tasking = []
        for index,task in enumerate(tasks):
            
            tasking.append([task[0],task[1],index])
         
        tasks = sorted(tasking) 
        index = 0
        while index < len(tasks):
            
            if tasks[index][0] <= start:
                
                heappush(heap,[tasks[index][1],tasks[index][2]])
                index += 1
             
            elif heap:
            
                current = heappop(heap)
                start += current[0]
                task_order.append(current[1])
                
            else:
                
                start = tasks[index][0]
                heappush(heap,[tasks[index][1],tasks[index][2]])
                index += 1
                
        while heap:
            
            task_order.append(heappop(heap)[1])
            
        return task_order