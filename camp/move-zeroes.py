class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, n in enumerate(nums):
            if n == 0:
                nums.pop(nums.index(n))
                nums.append(n)
                
        