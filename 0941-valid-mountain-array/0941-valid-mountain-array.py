class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3 or arr.index(max(arr)) == 0 or arr.index(max(arr)) == len(arr)-1:
            return False

        max_=0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                max_=i
                break
            elif arr[i] == arr[i+1]:
                return False
            
        for i in range(max_,len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
            
        
        return True