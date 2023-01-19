class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        size=len(nums)
        for i in range(size):
            nums.append(int(str(nums[i])[::-1]))
        
        return len(set(nums))