class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        
        for i in nums1:
            tmp = nums2.index(i)+1
            
            for j in range(tmp,len(nums2)):
                if nums2[j] > i:
                    ans[nums1.index(i)] = nums2[j]
                    break
                
        
        return ans