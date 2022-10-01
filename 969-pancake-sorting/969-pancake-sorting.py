class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        output=[]
        def flip(end):
            start=0
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
                
        for i in range(len(arr)-1,-1,-1):
            lrg=i
            
            for j in range(i,-1,-1):
                if arr[lrg] < arr[j]: lrg=j
            if lrg != i:
                flip(lrg)
                output.append(lrg+1)
                flip(i)
                output.append(i+1)
                
        return output
                