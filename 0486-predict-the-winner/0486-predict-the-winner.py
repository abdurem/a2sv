class Solution:
    def compare(self,nums,turn):
        if len(nums) == 1:
            if turn == False:
                return [nums[0],0]
            else:
                return [0,nums[0]]
        else:
            [p1,p2] = self.compare(nums[1:],not turn)
            [p3,p4] = self.compare(nums[:-1],not turn)
            if turn == False:
                return [max(nums[0]+p1,nums[-1]+p3),min(p2,p4)]
            else:
                return [min(p1,p3),max(nums[0]+p2,nums[-1]+p4)]  
    
    def PredictTheWinner(self, nums) -> bool:
        [p1,p2] = self.compare(nums,False)
        return True if p1 >= p2 else False