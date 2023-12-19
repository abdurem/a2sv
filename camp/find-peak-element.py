class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
            elif i == 1 and nums[i] < nums[i-1]:
                return 0
            elif i == len(nums)-2 and nums[i] < nums[i+1]:
                return i+1