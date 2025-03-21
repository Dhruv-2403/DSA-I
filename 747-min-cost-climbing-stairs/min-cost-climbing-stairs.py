class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        prev, curr = 0, 0 
        
        for i in range(2, n + 1):  
            next_step = min(curr + cost[i - 1], prev + cost[i -2])
            prev, curr = curr, next_step 
        
        return curr


        