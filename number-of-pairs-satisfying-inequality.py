class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        ans = 0

        for i in range(len(nums1)):
            arr.append(nums1[i] - nums2[i])

        def merge(left_half, right_half):
            nonlocal ans
            l = len(left_half) - 1
            r = len(right_half) - 1

            while  l >= 0:
                ans += (len(right_half) - r -1)

                while left_half[l] - diff <= right_half[r] and r >=0:
                    ans +=1
                    r -= 1
                l -=1                    

            l = r = 0
            sortedList = []
            while l < len(left_half) and r < len(right_half):
                if left_half[l] < right_half[r]:
                    sortedList.append(left_half[l])
                    l += 1
                else:
                    sortedList.append(right_half[r])
                    r += 1

            if l < len(left_half):
                sortedList.extend(left_half[l:])
            if r < len(right_half):
                sortedList.extend(right_half[r:])

            return sortedList


        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid+1, right, arr)

            return merge(left_half, right_half)

        mergeSort(0, len(arr) - 1, arr)
        return ans