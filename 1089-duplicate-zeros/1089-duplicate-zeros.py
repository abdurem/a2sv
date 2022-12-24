class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        index=0
        while index < len(arr)-1:
            if arr[index]==0:
                arr[index+1:]=[0]+arr[index+1:-1]
                index+=2
            else:
                index+=1