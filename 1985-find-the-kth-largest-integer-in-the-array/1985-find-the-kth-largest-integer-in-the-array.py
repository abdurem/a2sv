class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(reverse=True, key= lambda e: int(e))
        return nums[k-1]