class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums=[]
        ops={'+':lambda x,y: x+y, '-':lambda x,y: x-y, '*':lambda x,y: x*y, '/':lambda x,y: x/y}
        for token in tokens:
            if token in '+*-/':
                n1=nums.pop()
                n2=nums.pop()
                nums.append(int(ops[token](n2,n1)))
                continue
            nums.append(int(token))
        return nums[0]