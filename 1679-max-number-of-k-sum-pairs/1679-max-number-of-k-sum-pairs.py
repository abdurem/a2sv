class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans=0
        for i in count:
            ans+=min(count[i],count[k-i])
        
        return ans//2
                