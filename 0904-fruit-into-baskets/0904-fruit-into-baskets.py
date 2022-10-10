class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #[1123334411222]
        last_fruit=-1
        second_last_fruit=-1
        last_fruit_count=0
        mx=0
        cur=0
        
        for f in fruits:
            
            if f == last_fruit or f == second_last_fruit:
                cur+=1
            else:
                cur=last_fruit_count+1
            
            if f == last_fruit:
                last_fruit_count+=1
            else:
                last_fruit_count=1
            if f != last_fruit:
                second_last_fruit=last_fruit
                last_fruit = f
            mx=max(cur,mx)
        return mx