class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans=0
        seen= set()
        for i in count:
            if k-i in count and i not in seen:
                if i == (k-i):
                    ans += count[i]//2
                    seen.add(i)
                    continue
                else:
                    ans+= min(count[i],count[k-i])
                    seen.add(i)
                    seen.add(k-i)
        
        return ans
                