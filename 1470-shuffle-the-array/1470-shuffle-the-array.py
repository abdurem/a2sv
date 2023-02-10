class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1=nums[:n]
        arr2=nums[n:]
        ans=[]
        for i in range(n):
            ans.append(arr1[i])
            ans.append(arr2[i])
        return ans