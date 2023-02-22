class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        sm=0
        prev=0
        self.arr=[0]
        for i in nums:
            sm=i+prev
            prev=sm
            self.arr.append(prev)

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1]-self.arr[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)