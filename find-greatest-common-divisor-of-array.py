class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        while smallest != 0:
            temp = smallest
            smallest = largest % smallest
            largest = temp

        return largest