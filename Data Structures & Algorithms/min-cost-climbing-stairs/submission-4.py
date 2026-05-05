class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ''' 
        Top-down approach going in opposite direction

        Time: Optimised
        Space: Optimised

        However, cost array changed
        '''
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i +1], cost[i + 2])
        
        return min(cost[0], cost[1])
        