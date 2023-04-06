class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for i in nums:
            if nums[i] == 1:
                return i