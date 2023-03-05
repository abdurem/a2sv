class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1

        while l <= r:
            mid = (l+r)//2
            print(mid)
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                l = mid
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                r = mid
            else:
                return mid