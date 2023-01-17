class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            minIndex = i
            height=heights[i]
            name=names[i]
            for j in range(i-1,-1,-1):
                if height > heights[j]:
                    heights[minIndex] = heights[j]
                    names[minIndex] = names[j]
                    minIndex-=1
                else:
                    break
            heights[minIndex] = height
            names[minIndex] = name
                            
        return names