class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_=arr[-1]
        for i in range(len(arr)-1,-1,-1):
            tmp=arr[i]
            arr[i] = max_
            if tmp > max_:
                max_ = tmp
        arr[-1] = -1
        return arr
                