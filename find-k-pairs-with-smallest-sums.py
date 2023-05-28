class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)
        minn = min(len(nums1), k)
        for i in range(minn):
            heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        
        ans = []
        
        while k > 0 and heap:
            summ, num1, num2, indx = heappop(heap)
            ans.append([num1, num2])
            
            if indx < len(nums2) - 1:
                heappush(heap, (num1 + nums2[indx+1], num1, nums2[indx + 1], indx + 1))
            k -=1
        return ans