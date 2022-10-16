class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lft=0
        c=0
        mx=0
        for rgt in range(len(nums)):
            if nums[rgt] == 0:
                c+=1
            if c == 2:
                while True:
                    if nums[lft]== 0:
                        lft+=1
                        c=1
                        break 
                    lft+=1
            mx=max(mx,rgt-lft)
        print(mx)
        return mx