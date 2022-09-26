class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        i=0
        ans=[]
        vals=[]
        for val in sorted(count.values(), reverse=True):
            vals.append(val)
            i+=1
            if i == k:
                break
        for j in count:
            if count[j] in vals:
                ans.append(j)
        return ans