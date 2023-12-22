class Solution:
    def nextPermutation(self, nums):
        ind1 = -1
        ind2 = -1

        # Step 1: Find the breaking point
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind1 = i
                break

        # If there is no breaking point
        if ind1 == -1:
            self.reverse(nums, 0)
        else:
            # Step 2: Find the next greater element and swap with ind2
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[ind1]:
                    ind2 = i
                    break

            nums[ind1], nums[ind2] = nums[ind2], nums[ind1]

            # Step 3: Reverse the rest of the right half
            self.reverse(nums, ind1 + 1)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
