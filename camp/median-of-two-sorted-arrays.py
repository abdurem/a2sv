class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = self.divide(nums1, nums2)
        n = len(ans)

        if n%2 == 0:
            return (ans[(n//2)-1]+ ans[n//2])/2
        
        return ans[n//2]
    
    def divide(self, nums1, nums2):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        
        ans = []
        if nums1[0] > nums2[0]:
            ans.append(nums2[0])
            ans += self.divide(nums1, nums2[1:])
        else:
            ans.append(nums1[0])
            ans += self.divide(nums1[1:], nums2)
        
        return ans