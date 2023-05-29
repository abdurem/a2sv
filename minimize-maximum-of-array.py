class Solution:
    def minimizeArrayValue(self, arr: List[int]) -> int:
        ans = 0
        i = 1
        summ = arr[0]
        n = len(arr)
        while n-i:
            small = ceil(summ/i)
            summ += arr[i]
            i += 1
            new_small = ceil(summ/i)
            ans = max(ans, small, new_small)
        return ans