class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        r=0
        full=0
        for i in nums:
            full+=i
        print(f'full={full}')
        for i in range (len(nums)):
            r=full-nums[i]-l
            if r == l:
                return i
            l+=nums[i]
        
        return -1