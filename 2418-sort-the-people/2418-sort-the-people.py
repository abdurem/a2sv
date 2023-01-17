class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            minIndex=i
            for j in range(i,len(heights)):
                if heights[minIndex] < heights[j]:
                    minIndex=j
            heights[i],heights[minIndex] = heights[minIndex], heights[i]
            names[i],names[minIndex] = names[minIndex], names[i]
                
        return names