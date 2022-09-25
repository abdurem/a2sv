class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        pairs=0

        for i in count:
            pairs+=int(count[i]*(count[i]-1)/2)
            
        return pairs
        
        