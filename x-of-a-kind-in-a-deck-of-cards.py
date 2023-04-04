class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        frequency_dict = {}
        for card in deck:
            if card in frequency_dict:
                frequency_dict[card] += 1
            else:
                frequency_dict[card] = 1

        def calculate_hcf(nums):
            if len(nums) == 1:
                return nums[0]

            hcf = gcd(nums[0], nums[1])

            if len(nums) == 2:
                return hcf

            for i in range(1, len(nums) - 1):
                hcf = gcd(hcf, nums[i + 1])
                if hcf == 1:
                    return hcf
            return hcf

        hcf = calculate_hcf(list(frequency_dict.values()))

        return hcf > 1